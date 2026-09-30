## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4557.3.9.102.0
-  __TEXT.__text: 0xa0264
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0xe304
+4557.4.7.100.0
+  __TEXT.__text: 0xa6700
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_methlist: 0xe364
   __TEXT.__const: 0xa08
-  __TEXT.__gcc_except_tab: 0x9ac
-  __TEXT.__cstring: 0xa662
+  __TEXT.__gcc_except_tab: 0x9c4
+  __TEXT.__cstring: 0xa6a3
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x4581
-  __TEXT.__unwind_info: 0x3060
+  __TEXT.__unwind_info: 0x3338
   __TEXT.__objc_classname: 0x3e4b
-  __TEXT.__objc_methname: 0x23f8e
-  __TEXT.__objc_methtype: 0x6129
-  __TEXT.__objc_stubs: 0x16d00
+  __TEXT.__objc_methname: 0x24258
+  __TEXT.__objc_methtype: 0x61d8
+  __TEXT.__objc_stubs: 0x16de0
   __DATA_CONST.__got: 0x1040
   __DATA_CONST.__const: 0x2c68
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x4c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7aa8
+  __DATA_CONST.__objc_selrefs: 0x7af8
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xb28
+  __AUTH_CONST.__auth_got: 0xb08
   __AUTH_CONST.__const: 0x940
-  __AUTH_CONST.__cfstring: 0x9ee0
-  __AUTH_CONST.__objc_const: 0x2ce30
+  __AUTH_CONST.__cfstring: 0x9f20
+  __AUTH_CONST.__objc_const: 0x2ce98
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x4dd0
-  __DATA.__objc_ivar: 0xcf4
+  __DATA.__objc_ivar: 0xcfc
   __DATA.__data: 0x3928
   __DATA.__bss: 0x3d8
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C52CAF19-9F9B-3956-94CD-A0DDAF840131
-  Functions: 4618
-  Symbols:   17488
-  CStrings:  9516
+  UUID: DD39E099-4FFA-3BB5-B332-7428C6DEAE52
+  Functions: 4663
+  Symbols:   17619
+  CStrings:  9536
 
Symbols:
+ -[SBUISFloatingDockFileStackActionContext contentOverlayFrame]
+ -[SBUISFloatingDockFileStackActionContext initWithUUID:iconIdentifier:actionType:contentOverlayFrame:]
+ -[SBUISFloatingDockFileStackActionContext initWithUUID:iconIdentifier:actionType:toIconURL:fromSecurityURLWrappers:thumbnail:contentOverlayFrame:]
+ -[SBUISFloatingDockFileStackActionContext initWithUUID:iconIdentifier:actionType:toIconURL:fromSecurityURLWrappers:thumbnail:contentOverlayFrame:preferredDisplayName:]
+ -[SBUISFloatingDockFileStackActionContext initWithUUID:iconIdentifier:actionType:toPreferredDisplayName:]
+ -[SBUISFloatingDockFileStackActionContext preferredDisplayName]
+ -[SBUISFloatingDockRemoteContentHostComponent sceneWillDeactivate:withContext:]
+ _OBJC_IVAR_$_SBUISFloatingDockFileStackActionContext._contentOverlayFrame
+ _OBJC_IVAR_$_SBUISFloatingDockFileStackActionContext._preferredDisplayName
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _objc_msgSend$clientRequestToUpdateFileStackIcon:contentOverlayFrame:
+ _objc_msgSend$clientRequestToUpdateFileStackIcon:preferredDisplayName:
+ _objc_msgSend$clientWillDeactivateWithContext:
+ _objc_msgSend$contentOverlayFrame
+ _objc_msgSend$initWithUUID:iconIdentifier:actionType:toIconURL:fromSecurityURLWrappers:thumbnail:contentOverlayFrame:
+ _objc_msgSend$initWithUUID:iconIdentifier:actionType:toIconURL:fromSecurityURLWrappers:thumbnail:contentOverlayFrame:preferredDisplayName:
+ _objc_msgSend$preferredDisplayName
- _SBGetPowerDownViewMetrics.cold.1
- _objc_claimAutoreleasedReturnValue
- _objc_release_x6
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
CStrings:
+ "@104@0:8@16@24Q32@40@48@56{CGRect={CGPoint=dd}{CGSize=dd}}64@96"
+ "@72@0:8@16@24Q32{CGRect={CGPoint=dd}{CGSize=dd}}40"
+ "@96@0:8@16@24Q32@40@48@56{CGRect={CGPoint=dd}{CGSize=dd}}64"
+ "T@\"NSString\",R,C,N,V_preferredDisplayName"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_contentOverlayFrame"
+ "_contentOverlayFrame"
+ "_preferredDisplayName"
+ "clientRequestToUpdateFileStackIcon:contentOverlayFrame:"
+ "clientRequestToUpdateFileStackIcon:preferredDisplayName:"
+ "clientWillDeactivateWithContext:"
+ "contentOverlayFrame"
+ "initWithUUID:iconIdentifier:actionType:contentOverlayFrame:"
+ "initWithUUID:iconIdentifier:actionType:toIconURL:fromSecurityURLWrappers:thumbnail:contentOverlayFrame:"
+ "initWithUUID:iconIdentifier:actionType:toIconURL:fromSecurityURLWrappers:thumbnail:contentOverlayFrame:preferredDisplayName:"
+ "initWithUUID:iconIdentifier:actionType:toPreferredDisplayName:"
+ "kFloatingDockFileStackActionContextContentOverlayFrameKey"
+ "kFloatingDockFileStackActionContextPreferredDisplayNameKey"
+ "operation:captureInterrupted:"
+ "preferredDisplayName"
- "SBUIPowerDownView.m"
- "metrics"
- "void SBGetPowerDownViewMetrics(SBUIPowerDownViewMetrics *, BOOL)"

```
