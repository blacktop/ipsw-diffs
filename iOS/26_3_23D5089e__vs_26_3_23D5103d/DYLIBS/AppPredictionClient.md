## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-619.16.0.0.0
-  __TEXT.__text: 0x190718
+619.18.0.0.0
+  __TEXT.__text: 0x190938
   __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_methlist: 0x18d74
   __TEXT.__const: 0x6f8
   __TEXT.__cstring: 0x1bc3f
-  __TEXT.__oslogstring: 0x17a08
+  __TEXT.__oslogstring: 0x17b19
   __TEXT.__gcc_except_tab: 0x232c
   __TEXT.__dlopen_cstrs: 0x42d
   __TEXT.__ustring: 0x18a

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3352F3ED-C90A-3A02-B1CA-4D7DD7EAEB19
+  UUID: 1E31978D-25FB-3EE0-8C16-B4EB006ED1C4
   Functions: 10728
   Symbols:   35277
-  CStrings:  16106
+  CStrings:  16111
 
Functions:
~ -[ATXAppDirectoryClient getDirectoryResponseFromCacheWithMaxNumberOfAppsToPredict:] : 1680 -> 1892
~ +[ATXAppDirectoryResponse _canUseSuggestedApp:includeRemoteApps:] : 152 -> 484
CStrings:
+ "App Library Recently Added pod: %{public}@"
+ "App Library Suggestions pod: %{public}@"
+ "Bundle identifier is hidden by user preference: %{public}@"
+ "Siri settings Suggest App preference DISABLED for app: %{public}@"
+ "Siri settings Suggest App preference ENABLED for app: %{public}@"

```
