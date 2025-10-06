## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-614.0.24.0.0
-  __TEXT.__text: 0x37358
+614.40.23.0.0
+  __TEXT.__text: 0x37554
   __TEXT.__auth_stubs: 0x1330
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0x4e8
-  __TEXT.__oslogstring: 0x2d9d
+  __TEXT.__oslogstring: 0x2e07
   __TEXT.__cstring: 0x7cc3
-  __TEXT.__gcc_except_tab: 0xdb4
+  __TEXT.__gcc_except_tab: 0xdb8
   __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__unwind_info: 0x8a4
   __TEXT.__objc_classname: 0x2a9
   __TEXT.__objc_methname: 0x43cc
   __TEXT.__objc_methtype: 0x9ad

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 122468E0-A9D4-3085-A0E7-E8D84958F663
-  Functions: 827
-  Symbols:   3202
-  CStrings:  3602
+  UUID: FBE17748-AA98-36D2-A13C-F42BDD4AE0CF
+  Functions: 830
+  Symbols:   3209
+  CStrings:  3603
 
Symbols:
+ -[OSASystemConfiguration getPrefsKey:forDomain:withOptions:].cold.5
+ GCC_except_table90
+ _getACAccountTypeIdentifierExchange
+ _getACAccountTypeIdentifierExchange.cold.1
CStrings:
+ "Attempted xpc_user_sessions_get_foreground_uid() while fetching preferences for key %{public}@ but failed with error %{public}d - %{public}s"
+ "Failed to retrieve a valid user to access preferences container for key %{public}@"
- "fetching from defaults attempted xpc_user_sessions_get_foreground_uid() but failed with error %{public}d - %{public}s"

```
