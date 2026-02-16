## CaptiveNetwork

> `/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork`

```diff

-514.80.3.0.1
-  __TEXT.__text: 0xa378
-  __TEXT.__auth_stubs: 0x800
+514.100.16.0.0
+  __TEXT.__text: 0xa408
+  __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x67f
+  __TEXT.__cstring: 0x670
   __TEXT.__oslogstring: 0x70b
-  __TEXT.__unwind_info: 0x2c0
-  __TEXT.__eh_frame: 0x48
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methname: 0x2c
   __TEXT.__objc_methtype: 0x46

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__cfstring: 0x860
   __AUTH_CONST.__objc_const: 0x40
   __DATA.__data: 0x150
   __DATA.__bss: 0x78

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00B37476-ECBD-3D95-9B4A-B36074A4E335
-  Functions: 210
-  Symbols:   627
-  CStrings:  235
+  UUID: C535BD1F-CE6F-3CCF-A185-667DD1495DAB
+  Functions: 215
+  Symbols:   639
+  CStrings:  237
 
Symbols:
+ _CFStringCreateMutableCopy
+ _CFStringReplace
+ _CopyRedactedString
+ _OUTLINED_FUNCTION_0
Functions:
~ ___CNMonitorSetQueueAndHandler_block_invoke : 484 -> 476
+ _OUTLINED_FUNCTION_0
~ _my_CFArrayFindDictWithKeyAndValue : 156 -> 148
+ _CopyRedactedString
~ ___CNNetworkCopyDebugDesc : 236 -> 200
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_0
~ ___add_signal_port_source_block_invoke_2 : 532 -> 536
+ _OUTLINED_FUNCTION_0
~ _CNPluginMonitorStop.cold.1 : 20 -> 4
~ _CNNetworkGetTypeID.cold.1 : 20 -> 4
~ _CNPluginResponseGetTypeID.cold.1 : 20 -> 4
~ _CNScanListFilterStop.cold.1 : 20 -> 4
CStrings:
+ "*"
+ "<CNNetwork [%s] [signal %g] %s%p>"
- "<CNNetwork SSID %@ BSSID %@ [%s] [signal %g] %s%p>"

```
