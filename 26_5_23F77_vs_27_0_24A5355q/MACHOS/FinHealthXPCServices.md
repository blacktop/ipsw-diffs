## FinHealthXPCServices

> `/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices`

```diff

-1.8.5.1.0
-  __TEXT.__text: 0x1371c
-  __TEXT.__auth_stubs: 0x5f0
+1.9.1.22.0
+  __TEXT.__text: 0x12390
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_stubs: 0x3580
-  __TEXT.__objc_methlist: 0xd74
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x510
-  __TEXT.__objc_methname: 0x46b7
-  __TEXT.__cstring: 0x103b
-  __TEXT.__oslogstring: 0xcf3
-  __TEXT.__objc_classname: 0x13b
-  __TEXT.__objc_methtype: 0xe09
-  __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x730
+  __TEXT.__objc_methlist: 0xd80
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x4b4
+  __TEXT.__objc_methname: 0x46e9
+  __TEXT.__cstring: 0x1014
+  __TEXT.__oslogstring: 0xcb9
+  __TEXT.__objc_classname: 0x12d
+  __TEXT.__objc_methtype: 0xe00
+  __TEXT.__unwind_info: 0x3c0
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1850
-  __DATA.__objc_selrefs: 0x1178
+  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x730
+  __DATA.__objc_const: 0x1858
+  __DATA.__objc_selrefs: 0x1180
   __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BAA8889-A66F-30F5-B07D-7BD09763F286
+  UUID: BD26ED68-2C5C-331F-9CF8-F7E0E237EB0A
   Functions: 259
-  Symbols:   356
+  Symbols:   358
   CStrings:  1063
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _FHTransactionAccountTypeToString
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "credentials:didUpdateRangingSuspensionReasons:"
+ "didReceiveProxCardPresentationRequestWithTransportIdentifier:userInfo:"
+ "q"
+ "v32@0:8@\"NSArray\"16@\"NSArray\"24"
+ "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
+ "v56@0:8@16q24q32@40@?48"
- "-[FinHealthStateController insertOrUpdateTransaction:]"
- "[%s]. Received transaction.identifier: %@ accountType: %@"
- "credential:forPaymentApplication:didUpdateRangingSuspensionReasons:"
- "v40@0:8@\"PKAppletSubcredential\"16@\"PKPaymentApplication\"24Q32"
- "v40@0:8@16@24Q32"
- "v56@0:8@16Q24q32@40@?48"

```
