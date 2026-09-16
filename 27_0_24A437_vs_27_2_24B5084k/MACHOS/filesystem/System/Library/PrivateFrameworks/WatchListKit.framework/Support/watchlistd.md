## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-952.0.1.0.0
-  __TEXT.__text: 0x28564
+952.10.6.0.0
+  __TEXT.__text: 0x286bc
   __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_stubs: 0x53c0
+  __TEXT.__objc_stubs: 0x5460
   __TEXT.__objc_methlist: 0x2684
-  __TEXT.__cstring: 0x47a8
-  __TEXT.__oslogstring: 0x2970
+  __TEXT.__cstring: 0x4815
+  __TEXT.__oslogstring: 0x29b4
   __TEXT.__objc_classname: 0x469
   __TEXT.__objc_methtype: 0xf98
-  __TEXT.__objc_methname: 0x60d7
+  __TEXT.__objc_methname: 0x6132
   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0xd40
   __TEXT.__unwind_info: 0xcd8
   __DATA_CONST.__const: 0x1368
-  __DATA_CONST.__cfstring: 0x3c40
+  __DATA_CONST.__cfstring: 0x3c60
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x4a8
-  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__got: 0x5b0
   __DATA.__objc_const: 0x4df8
-  __DATA.__objc_selrefs: 0x1c68
+  __DATA.__objc_selrefs: 0x1c90
   __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x510

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 905
-  Symbols:   2577
-  CStrings:  1983
+  Symbols:   2584
+  CStrings:  1992
 
Symbols:
+ _OBJC_CLASS_$_IntentProgressReporterObjC
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_TVASCapabilityRegistryObjC
+ _objc_msgSend$defaultBagV3
+ _objc_msgSend$isChildAccount
+ _objc_msgSend$isSimpleProfile
+ _objc_msgSend$prewarmBagV3
+ _objc_msgSend$registerWithCapabilities:
+ _objc_msgSend$responseStatusCode
- _OBJC_CLASS_$_IntentPlayEventReporterObjC
- _objc_msgSend$statusCode
Functions:
~ +[AMSBag(WLKAdditions) wlk_defaultBag] : 252 -> 316
~ -[WLDClientConnection prewarm] : 80 -> 116
~ -[WLDServer _init] : 148 -> 192
~ __54+[WLDPlaybackReporter _decorateVODSummary:completion:]_block_invoke.36 : 680 -> 664
~ +[WLDPlaybackReporter _donateIntentWithPlaybackSummary:andMetadata:] : 1152 -> 1280
~ -[WLDPlaybackManager _shouldPromptForBundleID:outAccessStatus:] : 564 -> 652
CStrings:
+ "WLDPlaybackManager: should not prompt becuase it is currently disabled on U13 accounts."
+ "WLDPlaybackReporter - Skipping donation for Simple Profile account."
+ "defaultBagV3"
+ "isChildAccount"
+ "isSimpleProfile"
+ "prewarmBagV3"
+ "registerWithCapabilities:"
+ "responseStatusCode"
+ "sp_personal"
+ "tricycle"
- "statusCode"
```
