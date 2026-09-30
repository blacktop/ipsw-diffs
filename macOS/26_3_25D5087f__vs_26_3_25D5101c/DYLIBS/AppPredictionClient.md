## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/Versions/A/AppPredictionClient`

```diff

-619.16.0.0.0
-  __TEXT.__text: 0x1afff4
+619.18.0.0.0
+  __TEXT.__text: 0x1b0174
   __TEXT.__auth_stubs: 0xcf0
   __TEXT.__objc_methlist: 0x1885c
   __TEXT.__const: 0x6f0
   __TEXT.__cstring: 0x1b74e
-  __TEXT.__oslogstring: 0x17221
+  __TEXT.__oslogstring: 0x172f7
   __TEXT.__gcc_except_tab: 0x1ef8
   __TEXT.__dlopen_cstrs: 0x2cc
   __TEXT.__ustring: 0x18a

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: ED423BD3-5A52-3A67-BF2B-C1BDD8723861
+  UUID: AA1260AB-B42E-3851-A03D-97D98E9C82C4
   Functions: 10693
   Symbols:   24093
-  CStrings:  15945
+  CStrings:  15949
 
Functions:
~ -[ATXAppDirectoryClient getDirectoryResponseFromCacheWithMaxNumberOfAppsToPredict:] : 1652 -> 1888
~ +[ATXAppDirectoryResponse _canUseSuggestedApp:includeRemoteApps:] : 552 -> 700
CStrings:
+ "App Library Recently Added pod: %{public}@"
+ "App Library Suggestions pod: %{public}@"
+ "Siri settings Suggest App preference DISABLED for app: %{public}@"
+ "Siri settings Suggest App preference ENABLED for app: %{public}@"

```
