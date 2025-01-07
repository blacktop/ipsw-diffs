## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3402.63.2.0.0
-  __TEXT.__text: 0x28c590
-  __TEXT.__auth_stubs: 0x6ce0
+3403.2.1.0.0
+  __TEXT.__text: 0x28ed18
+  __TEXT.__auth_stubs: 0x6d00
   __TEXT.__objc_methlist: 0x36c
   __TEXT.__const: 0x8302
-  __TEXT.__cstring: 0x7bec
-  __TEXT.__swift5_typeref: 0x4042
-  __TEXT.__oslogstring: 0x23667
-  __TEXT.__constg_swiftt: 0x5458
+  __TEXT.__cstring: 0x7c0c
+  __TEXT.__swift5_typeref: 0x4038
+  __TEXT.__oslogstring: 0x23697
+  __TEXT.__constg_swiftt: 0x5460
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x3d6b
+  __TEXT.__swift5_reflstr: 0x3dcb
   __TEXT.__swift5_assocty: 0xa28
   __TEXT.__swift5_proto: 0x454
   __TEXT.__swift5_types: 0x310
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x2a23
+  __TEXT.__objc_methname: 0x2a2a
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x2ed4
-  __TEXT.__swift5_capture: 0x3858
+  __TEXT.__swift5_fieldmd: 0x2ef8
+  __TEXT.__swift5_capture: 0x3894
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3750
-  __TEXT.__eh_frame: 0x33c4
-  __DATA_CONST.__auth_got: 0x3670
-  __DATA_CONST.__got: 0x1d90
-  __DATA_CONST.__auth_ptr: 0x1f88
-  __DATA_CONST.__const: 0xa658
+  __TEXT.__unwind_info: 0x3770
+  __TEXT.__eh_frame: 0x342c
+  __DATA_CONST.__auth_got: 0x3680
+  __DATA_CONST.__got: 0x1da0
+  __DATA_CONST.__auth_ptr: 0x1c18
+  __DATA_CONST.__const: 0xa6a8
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0xa818
-  __DATA.__objc_selrefs: 0xcf0
+  __DATA.__objc_const: 0xa878
+  __DATA.__objc_selrefs: 0xcf8
   __DATA.__objc_data: 0x12f8
-  __DATA.__data: 0xb858
+  __DATA.__data: 0xb888
   __DATA.__bss: 0x7a10
   __DATA.__common: 0x488
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5199
+  Functions: 5210
   Symbols:   374
-  CStrings:  2988
+  CStrings:  2991
 
CStrings:
+ "AmbiguousDetermineFlow#executeBasedOnPlaybackState got back non playing state for Shazam UI device, triggering Acoustic ID Flow"
+ "AmbiguousDetermineFlow#executeBasedOnPlaybackState got back non playing state, and device doesn't have Shazam UI, responding with nothing playing dialog"
+ "LNActionExecutorErrorDomain"
+ "OpenMediaItemFlow#execute detected app intent with invalid parameters, trying with updated version"
+ "OpenMediaItemFlow#execute updated app intent threw an error: %s"
+ "domain"
- "AmbiguousDetermineFlow#executeBasedOnPlaybackState got back non playing state for non-HomePod device, triggering Acoustic ID Flow"
- "AmbiguousDetermineFlow#executeBasedOnPlaybackState got back non playing state, and device is HomePod, responding with nothing playing dialog"
- "UpdateMediaAffinity+HandleIntentStrategy#makeIntentHandledResponse returning completionViewOutput with a dialog."

```
