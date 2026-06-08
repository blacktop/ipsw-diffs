## addressbooksyncd

> `/usr/libexec/addressbooksyncd`

```diff

-306.0.0.0.0
-  __TEXT.__text: 0x3e3e4
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x7980
+307.0.0.0.0
+  __TEXT.__text: 0x3c034
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_stubs: 0x7940
   __TEXT.__objc_methlist: 0x4578
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x9d4
-  __TEXT.__objc_methname: 0x84ec
-  __TEXT.__cstring: 0x2d93
-  __TEXT.__objc_classname: 0x647
+  __TEXT.__gcc_except_tab: 0x924
+  __TEXT.__objc_methname: 0x84b6
+  __TEXT.__cstring: 0x2d76
+  __TEXT.__objc_classname: 0x5fb
   __TEXT.__objc_methtype: 0x13f2
-  __TEXT.__oslogstring: 0x25ea
-  __TEXT.__unwind_info: 0x1170
-  __DATA_CONST.__auth_got: 0x638
-  __DATA_CONST.__got: 0x610
-  __DATA_CONST.__const: 0xec0
-  __DATA_CONST.__cfstring: 0x3340
+  __TEXT.__oslogstring: 0x25f2
+  __TEXT.__unwind_info: 0xd18
+  __DATA_CONST.__const: 0xe98
+  __DATA_CONST.__cfstring: 0x3300
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_nlcatlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_intobj: 0xb58
+  __DATA_CONST.__auth_got: 0x648
+  __DATA_CONST.__got: 0x610
   __DATA.__objc_const: 0x9520
-  __DATA.__objc_selrefs: 0x27d0
+  __DATA.__objc_selrefs: 0x27c0
   __DATA.__objc_ivar: 0x4e0
   __DATA.__objc_data: 0x1310
   __DATA.__data: 0x6f0

   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync
   - /System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C4E57EE9-92ED-38A7-B137-CBF9992D8CE0
-  Functions: 1635
-  Symbols:   405
-  CStrings:  3237
+  UUID: 744F804F-D022-3E61-A713-36FA48290A61
+  Functions: 1627
+  Symbols:   407
+  CStrings:  3230
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _objc_release_x10
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ "== Started AddressBookSync-307"
+ "No device available from PairedDeviceRegistry at present -- will not store sync states until pairing completes."
- "== Started AddressBookSync-306"
- "No device available from NanoRegistry at present -- will not store sync states until pairing completes."
- "b727ad95-5778-41b6-a9db-05e7289820ed"
- "d5834418-f4a0-4c74-aa38-8ed5f7765bd1"
- "initWithUUIDString:"
- "v24@?0@\"NSString\"8@\"NSUUID\"16"
- "waitForPairingStorePathPairingID:"

```
