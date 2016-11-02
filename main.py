from lxml import etree
import json

tree = etree.parse('content.xml')
root = tree.getroot()


def init_matrix(size):
	new_matrix = [[0] * size for i in range(size)]
	return new_matrix


def prepare_authors_structure():
	names = root.xpath("//Author/*[self::LastName or self::ForeName]/text()")
	zip_authors = set(zip(names[0::2], names[1::2]))
	authors_list = [{"id": i, "forename": y, "lastname": x, "coauth": {}} for i, (x, y) in enumerate(zip_authors)]
	for auth in authors_list:
		auth["fullname"] = "{},{}".format("".join(auth["forename"].split()),"".join(auth["lastname"].split()))
	return authors_list


def add_contribution(auth,coauth_id):
	if coauth_id in auth["coauth"]:
		auth["coauth"][coauth_id] += 1
	else:
		auth["coauth"][coauth_id] = 1

def print_matrix():
	print "\t",
	for auth in authors[:-1:]:
		print "{}\t".format(auth["fullname"]),
	print(authors[-1]["fullname"])
	for auth in authors:
		print "{}\t".format(auth["fullname"]),
		print "{}\t".format(matrix[auth["id"]])



if __name__ == "__main__":
	authors = prepare_authors_structure()
	matrix = init_matrix(len(authors))

	for auth in authors:
		auth_id = auth["id"]
		author_list = root.xpath("//AuthorList[descendant::ForeName='{}' and descendant::LastName='{}']".format(auth["forename"], auth["lastname"]))
		for al in author_list:
			spec_authors = al.xpath("Author")
			for au in spec_authors:
				sa_fore = au.xpath("ForeName[1]/text()")[0]
				sa_last = au.xpath("LastName[1]/text()")[0]
				coauth_ref = [a for a in authors if a["forename"] == sa_fore and a["lastname"] == sa_last][0]
				add_contribution(auth, coauth_ref["id"])
				matrix[auth_id][coauth_ref["id"]] += 1

print_matrix()
print("\nAuthors structure:")
print(json.dumps(authors, indent=1))
