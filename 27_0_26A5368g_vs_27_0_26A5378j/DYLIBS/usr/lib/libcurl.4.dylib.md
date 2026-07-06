## libcurl.4.dylib

> `/usr/lib/libcurl.4.dylib`

```diff

-  __TEXT.__text: 0x6c3f0
+  __TEXT.__text: 0x6c2f8
   __TEXT.__const: 0xee4
   __TEXT.__cstring: 0x10aa5
   __TEXT.__unwind_info: 0x1180
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _Curl_altsvc_parse : 1748 -> 1712
~ _getalnum : 180 -> 184
~ _Curl_base64_decode : 644 -> 592
~ _Curl_pollset_change : 224 -> 228
~ _Curl_pollset_check : 80 -> 84
~ _Curl_build_unencoding_stack : 660 -> 644
~ _check_gzip_header : 248 -> 236
~ _cf_setup_connect : 952 -> 960
~ _Curl_cookie_add : 3892 -> 4012
~ _Curl_dynhds_get : 144 -> 164
~ _Curl_range : 296 -> 284
~ _Curl_sasl_decode_mech : 232 -> 240
~ _unescape_word : 228 -> 212
~ _lookup : 152 -> 120
~ _curl_easy_option_by_id : 64 -> 52
~ _Curl_hexencode : 112 -> 104
~ _ftp_statemachine : 2384 -> 2388
~ _Curl_headers_push : 728 -> 720
~ _create_hostcache_id : 176 -> 168
~ _Curl_hsts_parse : 596 -> 576
~ _Curl_copy_header_value : 240 -> 236
~ _Curl_compareheader : 248 -> 244
~ _Curl_add_custom_headers : 872 -> 876
~ _Curl_http_req_set_reader : 864 -> 868
~ _Curl_http_header : 2792 -> 2780
~ _Curl_http_write_resp_hds : 3380 -> 3384
~ _Curl_input_digest : 168 -> 152
~ _Curl_output_aws_sigv4 : 3524 -> 3520
~ _canon_query : 776 -> 764
~ _imap_do : 1772 -> 1768
~ _imap_connect : 508 -> 500
~ _imap_matchresp : 212 -> 224
~ _imap_get_message : 196 -> 200
~ _Curl_h1_req_parse_read : 1188 -> 1252
~ _curl_mime_encoder : 144 -> 124
~ _Curl_mime_contenttype : 160 -> 168
~ _encoder_7bit_read : 112 -> 108
~ _formatf : 4848 -> 4872
~ _singlesocket : 1048 -> 1052
~ _parsenetrc : 1424 -> 1392
~ _Curl_check_noproxy : 1072 -> 1024
~ _parsedate : 1700 -> 1608
~ _pop3_connect : 492 -> 484
~ _pop3_get_message : 196 -> 200
~ _Curl_rtsp_parseheader : 872 -> 860
~ _rtsp_filter_rtp : 1116 -> 1088
~ _Curl_trc_opt : 340 -> 336
~ _smtp_connect : 464 -> 456
~ _smtp_get_message : 196 -> 200
~ _Curl_getn_scheme_handler : 172 -> 176
~ _curl_url_set : 1968 -> 1960
~ _sectransp_connect_common : 8980 -> 9036
~ _sectransp_set_default_ciphers : 776 -> 792
~ _Curl_ssl_getsessionid : 432 -> 468
~ _Curl_init_sslset_nolock : 240 -> 236
~ _DNtostr : 476 -> 472
~ _ASN1tostr : 1612 -> 1564
~ _do_pubkey : 1032 -> 1024
~ _OID2str : 356 -> 340
~ _Curl_auth_digest_get_pair : 284 -> 268
~ _Curl_auth_decode_digest_http_message : 1132 -> 1120
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.H1gtkn/Sources/curl/curl/lib/vtls/openssl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mNxuq1/Sources/curl/curl/lib/vtls/openssl.c"

```
