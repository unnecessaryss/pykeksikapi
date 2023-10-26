import aiohttp, json


class HttpClient:
    async def request(
        api_method: str, 
        http_method: str = 'POST',
        url: str = 'https://api.keksik.io/',
        data: dict = {},
        *args, 
        **kwargs
    ) -> dict:
        try:
            async with aiohttp.ClientSession() as session:
                outcome = await (
                    await session.request(
                        http_method, url + api_method, data=json.dumps(data), *args, **kwargs
                    )
                ).json()

        except Exception as exc:
            outcome = {
                'success': False,
                'error': 1000,
                'msg': f'unknown error: {exc}'
            }

        return outcome