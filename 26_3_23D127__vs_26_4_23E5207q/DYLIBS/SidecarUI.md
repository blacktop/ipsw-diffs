## SidecarUI

> `/System/Library/PrivateFrameworks/SidecarUI.framework/SidecarUI`

```diff

-376.1.0.0.0
-  __TEXT.__text: 0xd50
-  __TEXT.__auth_stubs: 0x1c0
+380.1.0.0.0
+  __TEXT.__text: 0xdc8
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x50
   __TEXT.__oslogstring: 0x94
   __TEXT.__cstring: 0x2b
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xd0
   __TEXT.__objc_classname: 0x9a
   __TEXT.__objc_methname: 0x948
   __TEXT.__objc_methtype: 0x20d

   __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x4c8

   - /System/Library/PrivateFrameworks/SidecarCore.framework/SidecarCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 824167F6-AD65-3F33-AFCE-8D3CCAE5D03E
+  UUID: 3819C497-6FE8-31DF-9C96-3DA6A7B4FF83
   Functions: 53
-  Symbols:   238
+  Symbols:   236
   CStrings:  164
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_release_x24
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ -[SidecarServiceViewController sidecarServiceSetSceneIdentifier:] : 252 -> 256
~ _SidecarPresenterLogSubsystem : 116 -> 124
~ -[SidecarServiceViewController sidecarServiceSetSceneIdentityToken:] : 252 -> 256
~ -[SidecarServiceViewController setAllowsDisplaySleep:] : 108 -> 112
~ -[SidecarServiceViewController sidecarServiceUpdateSupportedOrientations] : 124 -> 132
~ -[SidecarServiceViewController setBackgroundStyle:] : 92 -> 96
~ -[SidecarServiceViewController setWantsVolumeButtonEvents:] : 92 -> 96
~ ___59-[SidecarServiceViewController _notifyServiceAndTerminate:]_block_invoke : 160 -> 168
~ -[SidecarServiceViewController completeRequest:] : 132 -> 136
~ -[SidecarServiceViewController serviceReady] : 116 -> 124
~ -[SidecarServiceViewController observeValueForKeyPath:ofObject:change:context:] : 416 -> 412
~ -[SidecarServiceViewController sidecarServiceProviderHandleRequest:] : 92 -> 96
~ -[SidecarServiceViewController setRequest:] : 188 -> 192
~ -[SidecarServiceViewController request] : 16 -> 64
~ -[SidecarServiceViewController initWithNibName:bundle:] : 288 -> 300

```
