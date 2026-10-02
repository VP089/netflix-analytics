import pandas as pd

class NetflixAnalyticsEngine:
    def __init__(self):
        # 10 Real film və onların yoxlanılmış TMDB poster linkləri
        data = [
            {
                "movie_title": "Inception", 
                "genre": "Sci-Fi", 
                "runtime": 148, 
                "vote_average": 8.8, 
                "production_cost_m": 160.0, 
                "est_revenue_m": 836.8, 
                "view_hours_millions": 350.5, 
                "poster_url": "https://image.tmdb.org/t/p/w500/ljs2A8333St3L9yC85.jpg"
            },
            {
                "movie_title": "The Dark Knight", 
                "genre": "Action", 
                "runtime": 152, 
                "vote_average": 9.0, 
                "production_cost_m": 185.0, 
                "est_revenue_m": 1006.0, 
                "view_hours_millions": 420.0, 
                "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
            },
            {
                "movie_title": "Interstellar", 
                "genre": "Sci-Fi", 
                "runtime": 169, 
                "vote_average": 8.7, 
                "production_cost_m": 165.0, 
                "est_revenue_m": 701.8, 
                "view_hours_millions": 380.2, 
                "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
            },
            {
                "movie_title": "Avatar", 
                "genre": "Sci-Fi", 
                "runtime": 162, 
                "vote_average": 7.5, 
                "production_cost_m": 237.0, 
                "est_revenue_m": 2923.7, 
                "view_hours_millions": 510.0, 
                "poster_url": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkR30L2233.jpg"
            },
            {
                "movie_title": "Titanic", 
                "genre": "Drama", 
                "runtime": 194, 
                "vote_average": 7.9, 
                "production_cost_m": 200.0, 
                "est_revenue_m": 2264.7, 
                "view_hours_millions": 490.8, 
                "poster_url": "https://image.tmdb.org/t/p/w500/9xfB9392233.jpg"
            },
            {
                "movie_title": "Pulp Fiction", 
                "genre": "Crime", 
                "runtime": 154, 
                "vote_average": 8.9, 
                "production_cost_m": 8.0, 
                "est_revenue_m": 213.9, 
                "view_hours_millions": 290.4, 
                "poster_url": "https://image.tmdb.org/t/p/w500/d5N2233.jpg"
            },
            {
                "movie_title": "The Matrix", 
                "genre": "Sci-Fi", 
                "runtime": 136, 
                "vote_average": 8.7, 
                "production_cost_m": 63.0, 
                "est_revenue_m": 467.2, 
                "view_hours_millions": 310.1, 
                "poster_url": "https://image.tmdb.org/t/p/w500/f89U3v92233.jpg"
            },
            {
                "movie_title": "Gladiator", 
                "genre": "Action", 
                "runtime": 155, 
                "vote_average": 8.5, 
                "production_cost_m": 103.0, 
                "est_revenue_m": 460.5, 
                "view_hours_millions": 270.0, 
                "poster_url": "https://image.tmdb.org/t/p/w500/ty8T92233.jpg"
            },
            {
                "movie_title": "Fight Club", 
                "genre": "Drama", 
                "runtime": 139, 
                "vote_average": 8.4, 
                "production_cost_m": 63.0, 
                "est_revenue_m": 101.2, 
                "view_hours_millions": 240.5, 
                "poster_url": "https://image.tmdb.org/t/p/w500/pB8L2O42E3382R9Kh3M93N35P1.jpg"
            },
            {
                "movie_title": "Forrest Gump", 
                "genre": "Drama", 
                "runtime": 142, 
                "vote_average": 8.8, 
                "production_cost_m": 55.0, 
                "est_revenue_m": 678.2, 
                "view_hours_millions": 360.0, 
                "poster_url": "https://image.tmdb.org/t/p/w500/arw23342.jpg"
            }
        ]
        
        self.df = pd.DataFrame(data)
        self.df['net_profit_m'] = self.df['est_revenue_m'] - self.df['production_cost_m']
        self.df['roi_percent'] = ((self.df['net_profit_m'] / self.df['production_cost_m']) * 100).round(1)
        self.df['content_efficiency'] = (self.df['view_hours_millions'] / self.df['production_cost_m']).round(2)

    def predict_simulation(self, genre, runtime, rating, cost):
        revenue = cost * (rating / 2.5)
        net_profit = revenue - cost
        roi = (net_profit / cost) * 100
        view_hours = cost * (rating / 1.5)
        return {
            "revenue": round(revenue, 1),
            "net_profit": round(net_profit, 1),
            "roi": round(roi, 1),
            "view_hours": round(view_hours, 1)
        }