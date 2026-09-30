## SafariSafeBrowsing

> `/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing`

```diff

-620.2.4.10.7
-  __TEXT.__text: 0x500fc
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__gcc_except_tab: 0x57e4
-  __TEXT.__cstring: 0x1674
-  __TEXT.__const: 0x248
-  __TEXT.__oslogstring: 0x1c74
-  __TEXT.__unwind_info: 0x25e8
-  __TEXT.__objc_classname: 0x1eb
-  __TEXT.__objc_methname: 0x2338
-  __TEXT.__objc_methtype: 0x162f
-  __TEXT.__objc_stubs: 0x1720
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x608
-  __DATA_CONST.__objc_classlist: 0x68
+621.1.13.10.4
+  __TEXT.__text: 0x5fc88
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0xafc
+  __TEXT.__gcc_except_tab: 0x6944
+  __TEXT.__cstring: 0x1909
+  __TEXT.__const: 0x298
+  __TEXT.__oslogstring: 0x1d83
+  __TEXT.__unwind_info: 0x2b48
+  __TEXT.__objc_classname: 0x217
+  __TEXT.__objc_methname: 0x23ca
+  __TEXT.__objc_methtype: 0x1749
+  __TEXT.__objc_stubs: 0x1780
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x770
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x788
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x8f8
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2370
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x1ba0
+  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__const: 0x27d8
+  __AUTH_CONST.__cfstring: 0x1180
+  __AUTH_CONST.__objc_const: 0x18b0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x80
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x300
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x410

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2019
-  Symbols:   2425
-  CStrings:  870
+  Functions: 2267
+  Symbols:   2787
+  CStrings:  922
 
Symbols:
+ _OBJC_CLASS_$_NSMutableData
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ _objc_retainAutoreleasedReturnValue
- ___chkstk_darwin
CStrings:
+ "&desiredHashLength=FOUR_BYTES"
+ "&hashPrefixes="
+ "&names="
+ "&version="
+ "@120@0:8{ServiceStatus={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}i{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}{vector<SafeBrowsing::ServiceStatus::Connection, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=^{Connection}^{Connection}{__compressed_pair<SafeBrowsing::ServiceStatus::Connection *, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=^{Connection}}}{vector<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=^{DatabaseUpdaterStatus}^{DatabaseUpdaterStatus}{__compressed_pair<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus *, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=^{DatabaseUpdaterStatus}}}}16"
+ "API_ABUSE"
+ "BILLING"
+ "CLIENT_INCIDENT"
+ "CSD_DOWNLOAD_WHITELIST"
+ "CSD_WHITELIST"
+ "HIGH_CONFIDENCE_ALLOWLIST"
+ "Invalid response: sent a request for %zu databases, but only got %zu hash lists back."
+ "MALICIOUS_BINARY"
+ "Received response from %d server with status code %d"
+ "SOCIAL_ENGINEERING_PRIVATE"
+ "SUBRESOURCE_FILTER"
+ "SUSPICIOUS"
+ "TB,R,N,GisGlobalCache"
+ "TB,R,N,V_useV5"
+ "TB,R,N,V_useV5BatchGet"
+ "Using Safe Browsing V5 for provider."
+ "Using V5 batch get endpoint to fetch database updates."
+ "Using safe browsing v5 hash search."
+ "V5: Full hash is not in globalCache."
+ "Versions to use V5"
+ "Versions to use V5 Batch Get"
+ "_SSBDatabaseUpdateV5FetchDataSessionHandler"
+ "_useV5"
+ "_useV5BatchGet"
+ "api_abuse"
+ "appendBytes:length:"
+ "bad_optional_access was thrown in -fno-exceptions mode"
+ "billing"
+ "client_incident"
+ "csd_download_whitelist"
+ "csd_whitelist"
+ "dataWithCapacity:"
+ "gc"
+ "globalCache"
+ "googleShouldUseV5"
+ "high_confidence_allowlist"
+ "https://safebrowsing.googleapis.com/v5/hashes:search"
+ "https://safebrowsing.googleapis.com/v5alpha1/hashLists:batchGet"
+ "isGlobalCache"
+ "malicious_binary"
+ "mw"
+ "pha"
+ "se"
+ "social_engineering_private"
+ "subresource_filter"
+ "suspicious"
+ "useV5"
+ "useV5BatchGet"
+ "uws"
+ "{ServiceStatus=\"m_name\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"m_pid\"i\"m_activeTransactions\"{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::string *, std::allocator<std::string>>=\"__value_\"^v}}\"m_connections\"{vector<SafeBrowsing::ServiceStatus::Connection, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=\"__begin_\"^{Connection}\"__end_\"^{Connection}\"__end_cap_\"{__compressed_pair<SafeBrowsing::ServiceStatus::Connection *, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=\"__value_\"^{Connection}}}\"m_databaseUpdatersStatuses\"{vector<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=\"__begin_\"^{DatabaseUpdaterStatus}\"__end_\"^{DatabaseUpdaterStatus}\"__end_cap_\"{__compressed_pair<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus *, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=\"__value_\"^{DatabaseUpdaterStatus}}}}"
+ "{unique_ptr<Backend::Google::HashListsBatchGetResponseParser, std::default_delete<Backend::Google::HashListsBatchGetResponseParser>>=\"__ptr_\"{__compressed_pair<Backend::Google::HashListsBatchGetResponseParser *, std::default_delete<Backend::Google::HashListsBatchGetResponseParser>>=\"__value_\"^{HashListsBatchGetResponseParser}}}"
- "@120@0:8{ServiceStatus={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}i{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}{vector<SafeBrowsing::ServiceStatus::Connection, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=^{Connection}^{Connection}{__compressed_pair<SafeBrowsing::ServiceStatus::Connection *, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=^{Connection}}}{vector<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=^{DatabaseUpdaterStatus}^{DatabaseUpdaterStatus}{__compressed_pair<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus *, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=^{DatabaseUpdaterStatus}}}}16"
- "Received response from %d server"
- "substringWithRange:"
- "{ServiceStatus=\"m_name\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"{__rep=\"\"(?=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1}\"__r\"{__raw=\"__words\"[3Q]})}}}\"m_pid\"i\"m_activeTransactions\"{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::string *, std::allocator<std::string>>=\"__value_\"^v}}\"m_connections\"{vector<SafeBrowsing::ServiceStatus::Connection, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=\"__begin_\"^{Connection}\"__end_\"^{Connection}\"__end_cap_\"{__compressed_pair<SafeBrowsing::ServiceStatus::Connection *, std::allocator<SafeBrowsing::ServiceStatus::Connection>>=\"__value_\"^{Connection}}}\"m_databaseUpdatersStatuses\"{vector<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=\"__begin_\"^{DatabaseUpdaterStatus}\"__end_\"^{DatabaseUpdaterStatus}\"__end_cap_\"{__compressed_pair<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus *, std::allocator<SafeBrowsing::ServiceStatus::DatabaseUpdaterStatus>>=\"__value_\"^{DatabaseUpdaterStatus}}}}"

```
