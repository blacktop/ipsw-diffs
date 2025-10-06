## addressbooksyncd

> `/usr/libexec/addressbooksyncd`

```diff

-275.0.0.0.0
-  __TEXT.__text: 0x3543c
+277.0.0.0.0
+  __TEXT.__text: 0x35808
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_stubs: 0x6ec0
-  __TEXT.__objc_methlist: 0x3ad4
+  __TEXT.__objc_stubs: 0x6f60
+  __TEXT.__objc_methlist: 0x3b24
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0x6d8
-  __TEXT.__objc_methname: 0x79bc
-  __TEXT.__cstring: 0x2a2d
+  __TEXT.__objc_methname: 0x7b2c
+  __TEXT.__cstring: 0x2a4c
   __TEXT.__objc_classname: 0x60e
-  __TEXT.__objc_methtype: 0x1321
-  __TEXT.__oslogstring: 0x2174
-  __TEXT.__unwind_info: 0xbec
+  __TEXT.__objc_methtype: 0x1332
+  __TEXT.__oslogstring: 0x21de
+  __TEXT.__unwind_info: 0xbf0
   __DATA_CONST.__auth_got: 0x640
-  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0xd10
-  __DATA_CONST.__cfstring: 0x3240
+  __DATA_CONST.__cfstring: 0x3260
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xb58
-  __DATA.__objc_const: 0x98e0
-  __DATA.__objc_selrefs: 0x23a0
+  __DATA.__objc_const: 0x9920
+  __DATA.__objc_selrefs: 0x23d8
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x360
+  __DATA.__objc_classrefs: 0x368
   __DATA.__objc_superrefs: 0x170
-  __DATA.__objc_ivar: 0x48c
+  __DATA.__objc_ivar: 0x490
   __DATA.__objc_data: 0x1270
   __DATA.__data: 0x6f8
   __DATA.__bss: 0x158

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A58D6556-B00D-33E2-89B0-0F9131CA9806
-  Functions: 1496
-  Symbols:   399
-  CStrings:  3056
+  UUID: 00BEEF2B-7E33-3573-BAAA-572FC27C12C2
+  Functions: 1505
+  Symbols:   401
+  CStrings:  3070
 
Symbols:
+ _CNContactSensitiveContentConfigurationKey
+ _OBJC_CLASS_$_CNSensitiveContentConfiguration
+ _objc_retain_x27
- _objc_retain_x26
CStrings:
+ "-[ABSContactsSyncManager _applyWallpaperArchiveToContactIfPossible:wrapper:]"
+ "/\x02\x14"
+ "== Started AddressBookSync-277"
+ "Failed to archive sensitiveContentOverride"
+ "Failed to unarchive CNSensitiveContentConfiguration data blob"
+ "Signal coalescing delay has hit the maximum. Something may be wrong if a long sync is not expected."
+ "T@\"NSData\",&,N,V_sensitiveContentConfiguration"
+ "_applyPronounsToContact:contactWrapper:"
+ "_applySensitiveContentConfigurationIfPossible:wrapper:isNewContact:"
+ "_applyWallpaperArchiveToContactIfPossible:wrapper:"
+ "_applyWatchWallpaperToContactIfPossible:wrapper:"
+ "_processSpecialRulesFieldsForContact:wrapper:isNewContact:"
+ "_sensitiveContentConfiguration"
+ "hasSensitiveContentConfiguration"
+ "logNilIDAccountsInStore:"
+ "sensitiveContentConfiguration"
+ "setSensitiveContentConfiguration:"
+ "v36@0:8@16@24B32"
- "-[ABSContactsSyncManager applyWallpaperArchiveToContactIfPossible:wrapper:]"
- "/\x01\x14"
- "== Started AddressBookSync-275"
- "Signal coalesing delay has hit the maximum. Something may be wrong if a long sync is not expected."
- "applyWallpaperArchiveToContactIfPossible:wrapper:"
- "applyWatchWallpaperToContactIfPossible:wrapper:"

```
