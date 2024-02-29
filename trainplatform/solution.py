class Solution:    
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        # Combine arrival and departure times and sort them
        events = [(arr[i], 'arr') for i in range(n)] + [(dep[i], 'dep') for i in range(n)]
        events.sort()

        platforms_needed = 0
        current_platforms = 0

        for time, event_type in events:
            if event_type == 'arr':
                current_platforms += 1
            else:
                current_platforms -= 1

            platforms_needed = max(platforms_needed, current_platforms)

        return platforms_needed
