## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-720.2.6.0.0
-  __TEXT.__text: 0x3b738
+720.2.7.0.0
+  __TEXT.__text: 0x3b944
   __TEXT.__objc_methlist: 0x2504
-  __TEXT.__const: 0x4f4
+  __TEXT.__const: 0x504
   __TEXT.__gcc_except_tab: 0x654
   __TEXT.__cstring: 0x1758
-  __TEXT.__oslogstring: 0x68b5
+  __TEXT.__oslogstring: 0x6985
   __TEXT.__constg_swiftt: 0x278
   __TEXT.__swift5_typeref: 0x43c
   __TEXT.__swift5_capture: 0x12c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x1210
+  __TEXT.__unwind_info: 0x1218
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_const: 0x5f30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xa38
-  __AUTH.__objc_data: 0x170
+  __AUTH.__objc_data: 0x120
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x23c
   __DATA.__data: 0xcd0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x5a8
   __DATA_DIRTY.__bss: 0xf0
   __DATA_DIRTY.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1146
-  Symbols:   2047
-  CStrings:  535
+  Functions: 1147
+  Symbols:   2048
+  CStrings:  536
 
Symbols:
+ -[UNSSettingsGateway copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:withCompletion:]
+ _BBSectionSettingsCapabilitiesFromUNCNotificationSourceDescription
+ ___106-[UNSSettingsGateway copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:withCompletion:]_block_invoke
- -[UNSSettingsGateway copySectionSettingsFromSectionID:toSectionID:withCompletion:]
- ___82-[UNSSettingsGateway copySectionSettingsFromSectionID:toSectionID:withCompletion:]_block_invoke
CStrings:
+ "UNSNotificationSettingsService [%{public}@] Destination capabilities 0x%lx [ allowCriticalAlerts: %{BOOL}d, allowTimeSensitive: %{BOOL}d, supportsTimeSensitive: %{BOOL}d, allowMessages: %{BOOL}d ]"
```
