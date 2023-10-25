import aiohttp

class HttpClient:
    
    async def request(
        api_method: str, 
        http_method: str = 'POST', 
        *args, 
        **kwargs
    ) -> dict:
    
        url = 'https://api.keksik.io/'

        try:

            async with aiohttp.ClientSession() as session:

                outcome = await (
                    await session.request(
                        http_method, url + api_method, *args, **kwargs
                    )
                ).json()

        except Exception as exc:

            outcome = {
                'success': False,
                'error': 1000,
                'msg': f'unknown error: {exc}'
            }

        return outcome