## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-9.6.3.0.0
-  __TEXT.__text: 0x8b63dc
+9.6.5.0.0
+  __TEXT.__text: 0x8b74f4
   __TEXT.__auth_stubs: 0x49f0
-  __TEXT.__objc_methlist: 0x22ddc
+  __TEXT.__objc_methlist: 0x22dfc
   __TEXT.__const: 0xbc1b8
   __TEXT.__dlopen_cstrs: 0x88c
-  __TEXT.__cstring: 0x29be8
+  __TEXT.__cstring: 0x29c7c
   __TEXT.__swift5_typeref: 0x71e5
   __TEXT.__swift5_reflstr: 0x3b34
   __TEXT.__swift5_assocty: 0xf30

   __TEXT.__swift5_capture: 0x39c8
   __TEXT.__swift5_mpenum: 0x8c
   __TEXT.__swift5_protos: 0x110
-  __TEXT.__oslogstring: 0x2e8d1
+  __TEXT.__oslogstring: 0x2ea07
   __TEXT.__gcc_except_tab: 0x5914
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x12498
+  __TEXT.__unwind_info: 0x124b0
   __TEXT.__eh_frame: 0x17540
   __TEXT.__objc_classname: 0x5a84
-  __TEXT.__objc_methname: 0x46de5
+  __TEXT.__objc_methname: 0x46e65
   __TEXT.__objc_methtype: 0x90ee
-  __TEXT.__objc_stubs: 0x2f620
+  __TEXT.__objc_stubs: 0x2f680
   __DATA_CONST.__got: 0x19d0
-  __DATA_CONST.__const: 0x55d0
+  __DATA_CONST.__const: 0x55f0
   __DATA_CONST.__objc_classlist: 0x1508
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf2f8
+  __DATA_CONST.__objc_selrefs: 0xf310
   __DATA_CONST.__objc_protorefs: 0x240
   __DATA_CONST.__objc_superrefs: 0xcc0
   __DATA_CONST.__objc_arraydata: 0x498
   __AUTH_CONST.__auth_got: 0x2510
-  __AUTH_CONST.__const: 0x456e8
-  __AUTH_CONST.__cfstring: 0x22040
+  __AUTH_CONST.__const: 0x45748
+  __AUTH_CONST.__cfstring: 0x221a0
   __AUTH_CONST.__objc_const: 0x3d2f0
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x180

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 28039
-  Symbols:   30908
-  CStrings:  20420
+  Functions: 28047
+  Symbols:   30919
+  CStrings:  20438
 
Symbols:
+ +[AMSPushParsableEngagementEvent _currentPlatformString]
+ +[AMSPushParsableEngagementEvent _eventForMediaAPIPayload:clientIdentifier:account:bag:]
+ +[AMSPushParsableEngagementEvent _resolveMediaAPIPlaceholders:storefrontId:languageTag:]
+ __88+[AMSPushParsableEngagementEvent _eventForMediaAPIPayload:clientIdentifier:account:bag:]_block_invoke
+ ___88+[AMSPushParsableEngagementEvent _eventForMediaAPIPayload:clientIdentifier:account:bag:]_block_invoke
+ ___88+[AMSPushParsableEngagementEvent _eventForMediaAPIPayload:clientIdentifier:account:bag:]_block_invoke_2
+ ___88+[AMSPushParsableEngagementEvent _eventForMediaAPIPayload:clientIdentifier:account:bag:]_block_invoke_3
+ ___block_descriptor_40_e34_v24?0"AMSURLResult"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s_e29_"AMSPromise"16?0"NSArray"8l
+ _objc_msgSend$_currentPlatformString
+ _objc_msgSend$_eventForMediaAPIPayload:clientIdentifier:account:bag:
+ _objc_msgSend$_resolveMediaAPIPlaceholders:storefrontId:languageTag:
- ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0l
CStrings:
+ "%{public}@: [%{public}@] Fetching mediaAPI URL"
+ "%{public}@: [%{public}@] Finished mediaAPI request successfully"
+ "%{public}@: [%{public}@] Finished mediaAPI request with error %{public}@"
+ "%{public}@: [%{public}@] Found mediaAPI request"
+ "%{public}@: [%{public}@] Payload set mediaApi but clientIdentifier is not set"
+ "<private>"
+ "AppleTv"
+ "Desktop"
+ "Ipad"
+ "Iphone"
+ "MediaAPI URL Not Found"
+ "MediaAPI clientIdentifier Not Found"
+ "RealityDevice"
+ "_currentPlatformString"
+ "_eventForMediaAPIPayload:clientIdentifier:account:bag:"
+ "_resolveMediaAPIPlaceholders:storefrontId:languageTag:"
+ "acceptLanguage"
+ "mediaApi"
+ "{%@}"
- "seed"
```
