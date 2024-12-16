## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

```diff

-490.0.0.0.0
-  __TEXT.__text: 0x174f0
+490.80.1.502.1
+  __TEXT.__text: 0x179a8
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x2fc0
+  __TEXT.__objc_stubs: 0x2fe0
   __TEXT.__objc_methlist: 0xd80
-  __TEXT.__const: 0x62
-  __TEXT.__objc_methname: 0x2e5c
-  __TEXT.__oslogstring: 0x2a99
-  __TEXT.__cstring: 0x10b4
+  __TEXT.__const: 0x6a
+  __TEXT.__objc_methname: 0x2e99
+  __TEXT.__oslogstring: 0x2bac
+  __TEXT.__cstring: 0x110e
   __TEXT.__objc_classname: 0x190
-  __TEXT.__objc_methtype: 0x6f3
-  __TEXT.__gcc_except_tab: 0x494
-  __TEXT.__unwind_info: 0x478
+  __TEXT.__objc_methtype: 0x6fb
+  __TEXT.__gcc_except_tab: 0x4f4
+  __TEXT.__unwind_info: 0x488
   __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__got: 0x480
   __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__cfstring: 0x1040
+  __DATA_CONST.__cfstring: 0x1060
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x2af0
-  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_selrefs: 0xd28
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 420
-  Symbols:   1442
-  CStrings:  1074
+  Functions: 421
+  Symbols:   1446
+  CStrings:  1079
 
Symbols:
+ -[PKDPlugIn allowForClient:discoveryInstanceUUID:].cold.1
+ -[PKDPlugIn match:discoveryInstanceUUID:server:withError:]
+ -[PKDPlugIn matchDictionary:pattern:discoveryInstanceUUID:withError:]
+ -[PKDPlugIn matchKey:pattern:discoveryInstanceUUID:server:withError:]
+ GCC_except_table15
+ _OBJC_CLASS_$_NSError
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$match:discoveryInstanceUUID:server:withError:
+ _objc_msgSend$matchDictionary:pattern:discoveryInstanceUUID:withError:
+ _objc_msgSend$matchKey:pattern:discoveryInstanceUUID:server:withError:
- -[PKDPlugIn match:discoveryInstanceUUID:server:]
- -[PKDPlugIn matchDictionary:pattern:discoveryInstanceUUID:]
- -[PKDPlugIn matchKey:pattern:discoveryInstanceUUID:server:]
- _objc_msgSend$match:discoveryInstanceUUID:server:
- _objc_msgSend$matchDictionary:pattern:discoveryInstanceUUID:
- _objc_msgSend$matchKey:pattern:discoveryInstanceUUID:server:
CStrings:
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@16@24@32@40^@48"
+ "Unable to evaluate NSExtension against the rules, filter: %@ value: %@ with exception: %@"
+ "[d %@] [u %{public}@] [%@(%@)] Could not determine if plugin matched the exclusion rule: %@, error: %@"
+ "[d %@] [u %{public}@] [%@(%@)] Rule matching failed for the plugin, error: %@"
+ "[u %{public}@] [%@(%@)] The host's plug-in entitlement does not allow this plug-in, error: %@"
+ "errorWithDomain:code:userInfo:"
+ "match:discoveryInstanceUUID:server:withError:"
+ "matchDictionary:pattern:discoveryInstanceUUID:withError:"
+ "matchKey:pattern:discoveryInstanceUUID:server:withError:"
- "B40@0:8@16@24@32"
- "B48@0:8@16@24@32@40"
- "match:discoveryInstanceUUID:server:"
- "matchDictionary:pattern:discoveryInstanceUUID:"
- "matchKey:pattern:discoveryInstanceUUID:server:"

```
