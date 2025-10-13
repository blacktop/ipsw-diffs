## AppIntents

> `/System/Library/Frameworks/AppIntents.framework/AppIntents`

```diff

-300.1.10.0.0
-  __TEXT.__text: 0x419a64
-  __TEXT.__auth_stubs: 0x3950
+300.1.12.0.0
+  __TEXT.__text: 0x419aac
+  __TEXT.__auth_stubs: 0x3960
   __TEXT.__objc_methlist: 0x1408
   __TEXT.__dlopen_cstrs: 0x9a
-  __TEXT.__cstring: 0x7b89
+  __TEXT.__cstring: 0x7bb9
   __TEXT.__swift5_typeref: 0x114da
   __TEXT.__const: 0x28a88
   __TEXT.__constg_swiftt: 0x11550

   __TEXT.__swift5_types: 0xbf0
   __TEXT.__swift5_protos: 0x458
   __TEXT.__swift_as_entry: 0x1144
-  __TEXT.__oslogstring: 0x4518
+  __TEXT.__oslogstring: 0x4552
   __TEXT.__swift5_capture: 0x3c1c
   __TEXT.__swift_as_ret: 0x12c4
   __TEXT.__swift5_mpenum: 0x16c
-  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__unwind_info: 0x11538
   __TEXT.__eh_frame: 0x23d70
   __TEXT.__objc_classname: 0x2bc

   __DATA_CONST.__objc_selrefs: 0x1fb8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1cb8
+  __AUTH_CONST.__auth_got: 0x1cc0
   __AUTH_CONST.__const: 0x1be08
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x4d20

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7036E002-5071-3BA8-B3A9-AD0D173D1E41
+  UUID: EEE2EC07-F311-35DC-B002-770C11C6535C
   Functions: 28748
-  Symbols:   25118
-  CStrings:  2478
+  Symbols:   25119
+  CStrings:  2480
 
Symbols:
+ _geteuid
Functions:
~ -[LNProcessInstanceRegistryClient registerWithError:] : 856 -> 928
CStrings:
+ "Attempting to register during setup, linkd is not running"
+ "Empty Snippet should not be run"
+ "User needs to be connected to the internet"
- "Empty Snippet should not be ran"

```
