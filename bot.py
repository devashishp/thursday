from mastodon import Mastodon

mastodon = Mastodon (
        access_token = 'token.secret',
        api_base_url = 'https://botsin.space/'
        )

media = mastodon.media_post("media/thursday.jpg", description="Nadia from the Russian Doll fearing that she would never see a Thursday again says, \"Thursday. What a concept\" while smoking a cigarette")
mastodon.status_post("Thursday. What a concept.", media_ids=[media])
