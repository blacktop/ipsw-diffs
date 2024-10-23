## ShazamKitUI

> `/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI`

```diff

-301.8.0.0.0
-  __TEXT.__text: 0x2b1a0
-  __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_methlist: 0xb14
-  __TEXT.__const: 0x22f4
+304.0.0.0.0
+  __TEXT.__text: 0x2a1b8
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_methlist: 0xa14
+  __TEXT.__const: 0x2284
   __TEXT.__cstring: 0x106b
-  __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__oslogstring: 0x83
   __TEXT.__constg_swiftt: 0xb7c
-  __TEXT.__swift5_typeref: 0x2418
+  __TEXT.__swift5_typeref: 0x23ea
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x6d5
   __TEXT.__swift5_fieldmd: 0x73c
-  __TEXT.__swift5_assocty: 0x3e0
-  __TEXT.__swift5_proto: 0x100
+  __TEXT.__swift5_assocty: 0x3c8
+  __TEXT.__swift5_proto: 0xfc
   __TEXT.__swift5_types: 0xc8
   __TEXT.__swift5_capture: 0x2b8
+  __TEXT.__oslogstring: 0x23
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0xe18
+  __TEXT.__unwind_info: 0xda0
   __TEXT.__eh_frame: 0xcac
-  __TEXT.__objc_classname: 0x243
-  __TEXT.__objc_methname: 0x272c
-  __TEXT.__objc_methtype: 0x500
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__objc_classlist: 0xe0
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x38
+  __TEXT.__objc_classname: 0x1a6
+  __TEXT.__objc_methname: 0x2479
+  __TEXT.__objc_methtype: 0x385
+  __TEXT.__objc_stubs: 0x1900
+  __DATA_CONST.__got: 0x558
+  __DATA_CONST.__const: 0x290
+  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad0
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x230
-  __AUTH_CONST.__auth_got: 0xba8
-  __AUTH_CONST.__auth_ptr: 0x7c0
-  __AUTH_CONST.__const: 0x1300
+  __AUTH_CONST.__auth_got: 0xb40
+  __AUTH_CONST.__auth_ptr: 0x780
+  __AUTH_CONST.__const: 0x12c0
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x20e0
+  __AUTH_CONST.__objc_const: 0x1d48
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x190
-  __AUTH.__objc_data: 0x998
+  __AUTH.__objc_data: 0x8f8
   __AUTH.__data: 0x768
-  __DATA.__objc_ivar: 0x94
-  __DATA.__data: 0xfa0
-  __DATA.__bss: 0x20c0
+  __DATA.__objc_ivar: 0x88
+  __DATA.__data: 0xe18
+  __DATA.__bss: 0x2020
   __DATA.__common: 0x100
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1243
-  Symbols:   525
-  CStrings:  665
+  Functions: 1211
+  Symbols:   478
+  CStrings:  618
 
Symbols:
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_SHCoreError
- _OBJC_CLASS_$_SHError
- _OBJC_CLASS_$_SHMediaLibraryTrack
- _SHShazamKitUIServiceInterface
- _SHShazamKitUIServiceName
- __NSConcreteGlobalBlock
- __Unwind_Resume
- ___objc_personality_v0
- _dispatch_once
- _objc_copyWeak
- _objc_initWeak
- _objc_opt_new
- _objc_retainBlock
- _objc_retain_x4
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _shcore_log_object
CStrings:
- "\x12"
- "@\"NSXPCConnection\""
- "@\"NSXPCConnection\"16@0:8"
- "@\"SHShazamKitUIServiceConnectionProvider\""
- "Fired XPC service interruption handler %!@(MISSING)"
- "Fired XPC service invalidation handler %!@(MISSING)"
- "Presentation"
- "SHMediaItemPresentation"
- "SHMediaLibraryPresentation"
- "SHShazamKitUIService"
- "SHShazamKitUIServiceConnection"
- "SHShazamKitUIServiceConnectionProvider"
- "T@\"NSXPCConnection\",R,N,V_connection"
- "T@\"SHShazamKitUIServiceConnectionProvider\",R,N,V_connectionProvider"
- "T{os_unfair_lock_s=I},N,V_connectionLock"
- "_connection"
- "_connectionLock"
- "_connectionProvider"
- "attachDefaultConnectionHandlers"
- "connection"
- "connectionLock"
- "connectionProvider"
- "errorWithCode:underlyingError:"
- "initWithConnectionProvider:"
- "initWithMachServiceName:options:"
- "invalidate"
- "presentMediaLibraryWithCompletionHandler:"
- "remapErrorToClientError:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "scheduleSendBarrierBlock:"
- "setConnectionLock:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "sh_uiServerConnection"
- "shazamKitUIServiceConnection"
- "tearDownConnection"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"SHMediaItem\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"SHMediaItem\"16@\"SHMediaItemPresentationSettings\"24@?<v@?q@\"NSURL\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
