# various XPaths for competition info elements
COMPETITOR_LIMIT = '//*[@id="registration_requirements_text"]/text()[3]'
COMPETITORS_LIST = '//*[@id="competition-nav"]/div/a[3]'
COMPETITOR_TABLE_FOOTER = '//*[@id="competition-data"]/div/div[1]/div[2]/div[2]/table/tfoot/tr/td[1]'


class Competition:
    """Object to hold all information about a WCA competition"""
    def __init__(self, name, date, location, url, venue, d):
        # all attributes defined here can be found in the WCA competitions page
        # the @property methods find information that must be found on the competition's individual page.
        self.name = name
        self.date = date
        self.location = location
        self.url = url
        self.venue = venue
        
        # necessary for finding other info about competition
        self.driver = d


    @property
    def reached_competitor_limit(self):
        """tells if the competitor limit for the competition has been reached
        
        Returns:
            bool -- True if it has been reached, False if not
        """
        with self.driver as driver:
            driver.get(self.url)
            
            # find the line where the competitor limit is stated
            competitor_limit_line = driver.find_element_by_xpath(COMPETITOR_LIMIT)
            competitor_limit = int(competitor_limit_line.split(' ')[-2])
            # find the link to the competitor list
            competitor_list_url = driver.find_element_by_xpath(COMPETITORS_LIST).get_attribute('href')

            driver.get(competitor_list_url)

            # find bottom text of competitor table
            table_footer = driver.find_element_by_xpath(COMPETITOR_TABLE_FOOTER).text.strip()

            people = int(table_footer.split(' ')[-2])

            if people == competitor_limit:
                return True
            else:
                return False


    @property
    def venue_address(self):
        """Finds address to competition venue"""
        return ''
 

    @property
    def driving_distance(self):
        """Finds the driving distance from your location to the competition
        
        Args:
            current_location -- address of where you want to drive to the competition from

        Returns:
            str -- hours h minutes min
        """
        return ''

    def __str__(self):
        """Creates message containing complete information
        
        Message to be written to text file with other competitions
        """
        info_list = [
                ''.join(['=' for i in range(100)]),
                '',
                self.name.upper() + ':',
                self.url,
                '',
                f'date: {self.date}',
                f'location: {self.location}',
                f'venue: {self.venue} - {self.venue_address}',
                f'distance: {self.driving_distance}',
            ]
        
        if self.reached_competitor_limit:
            info_list.append('reached competitor limit')
        
        string = '\n'.join(info_list)

        return string

    __repr__ = __str__