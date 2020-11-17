# You have been provided with a log file, log.out which contains some entries.
# Each line has somewhat fixed formatting,
# Number IP Country Company Locale Continent
# We are concerned with the first three entries here.
# Complete the two functions below, analyze() and ips().
# analyze(), takes as input a file iterator and writes to stats dictionary.
# <key> : <value>
# country : [list of ips]
# ips() accepts a country and returns all the IPs associated with that country.
# If the country is not found in the dictionary then return empty list: []


stats = {

}

def analyze(f):
    for val in f:
        text = val.split("   ")
        ip = text[1]
        Country = text[2]

        if Country not in stats:
            stats[Country] = [ip]
        else:
            stats[Country].append(ip)

    return stats

def ips(Country):
    return stats.get(Country, [])


if __name__ == '__main__':
    f = open('./log.out', 'r')
    analyze(f)

    for country in ['USA', 'China', 'Germany', 'Australia']:
        print('{:15} -> {}'.format(country, ips(country)))