expected_export_chats_to_txt_raw_result = """Sung-Soo Kyler (+997863428668)\n\nMessage(message_id=158352, key_id='6BE2CB39DE7CE864C49F28F6B11EAD05', chat_id=533, from_me=1, sender_contact=Contact(raw_string_jid='997863428668@s.whatsapp.net', name='Sung-Soo Kyler', number='+997863428668'), timestamp=1543317689901, text_data='Nulla scelerisque leo augue, sit amet ullamcorper est aliquet sed!! 😂', media=Media(message_id=158352, media_job_uuid='fbc84a18-aacf-4bbe-a736-a968e5ca82e5', file_path='Media/WhatsApp Images/Sent/IMG-20181127-WA0025.jpg', mime_type=''), geo_position=None, reply_to=None)\nMessage(message_id=158353, key_id='FBCEBE15C475DCE9F74087D8735CABB0', chat_id=533, from_me=1, sender_contact=Contact(raw_string_jid='997863428668@s.whatsapp.net', name='Sung-Soo Kyler', number='+997863428668'), timestamp=1543317698865, text_data='Fusce mollis libero!!', media=None, geo_position=None, reply_to=None)\nMessage(message_id=158394, key_id='3D15299A2A6B62DBC5BEC42E42C9E48A', chat_id=456, from_me=1, sender_contact=Contact(raw_string_jid='997863428668@s.whatsapp.net', name='Sung-Soo Kyler', number='+997863428668'), timestamp=1580132486421, text_data='', media=None, geo_position=GeoPosition(message_id=158394, latitude=65.754409, longitude=-168.924534), reply_to='6BE2CB39DE7CE864C49F28F6B11EAD05')"""

expected_export_chats_to_txt_formatted_result = """Vivamus bibendum\n\n[2018-11-27 16:51:29.901000]: Me - Nulla scelerisque leo augue, sit amet ullamcorper est aliquet sed!! 😂\n\t>>> Media: Media/WhatsApp Images/Sent/IMG-20181127-WA0025.jpg\n[2018-11-27 16:51:38.865000]: Me - Fusce mollis libero!!\n[2020-01-27 19:11:26.421000]: Me\n\t>>> Reply to: Me - Nulla scelerisque leo augue, sit amet ullamcorper est aliquet sed!! 😂\n\t>>> Location: (65.754409,-168.924534)"""

expected_export_call_logs_to_txt_raw_result = """Izebel Bengtsdotter (+669233817152)\n\nCall(call_row_id=929, from_me=1, timestamp=1545829680246, video_call=0, duration=0, call_result=4)\nCall(call_row_id=2909, from_me=1, timestamp=1568973142212, video_call=0, duration=0, call_result=2)\nNone"""

expected_export_call_logs_to_txt_formatted_result = """Izebel Bengtsdotter (+669233817152)\n\n[2018-12-26 18:38:00]: Me ----> Izebel Bengtsdotter (+669233817152)\n\t>>> Call Type: 📞 - Voice Call\n\t>>> Duration: 00 seconds\n\t>>> Status: 4\n[2019-09-20 15:22:22]: Izebel Bengtsdotter (+669233817152) ----> Me\n\t>>> Call Type: 📞 - Voice Call\n\t>>> Duration: 01:12 minutes\n\t>>> Status: 2"""
