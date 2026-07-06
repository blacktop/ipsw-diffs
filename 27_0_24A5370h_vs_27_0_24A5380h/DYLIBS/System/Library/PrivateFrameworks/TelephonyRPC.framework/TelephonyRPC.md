## TelephonyRPC

> `/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`

```diff

-  __TEXT.__text: 0x1ccd4
+  __TEXT.__text: 0x1cd00
   __TEXT.__objc_methlist: 0x10b0
   __TEXT.__cstring: 0x18d4
   __TEXT.__const: 0x918
-  __TEXT.__oslogstring: 0xb43
+  __TEXT.__oslogstring: 0xb53
   __TEXT.__ustring: 0x5c
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__swift5_typeref: 0x408

   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift_as_cont: 0xc8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x790
+  __TEXT.__unwind_info: 0x798
   __TEXT.__eh_frame: 0xf20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc08
+  __DATA_CONST.__objc_selrefs: 0xc18
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x3a8
   __AUTH_CONST.__const: 0x968
   __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x1e80
+  __AUTH_CONST.__objc_const: 0x1e60
   __AUTH_CONST.__auth_got: 0x958
   __AUTH.__objc_data: 0x228
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x520
   __DATA.__bss: 0x788
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 604
-  Symbols:   1633
+  Symbols:   1635
   CStrings:  360
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$isCancelled
+ _objc_msgSend$waitUntilDate:
- _OBJC_IVAR_$_NPHVMSyncSessionManager._cancel
Functions:
~ -[NPHVMSyncSessionManager syncSession:enqueueChanges:error:] : 1276 -> 1280
~ -[NPHVMSyncSessionManager isCancelled] : 8 -> 12
~ -[VoicemailCompanionReplication handleSIGTERM] : 488 -> 524
CStrings:
+ "%s - exiting"
+ "%s - timed out waiting for sync to cancel; exiting anyway"
- "%s - done waiting"
- "%s - sync no longer in progress; exiting"

```
