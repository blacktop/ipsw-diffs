## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4552.106.0.0.0
-  __TEXT.__text: 0x9ea18
+4556.102.0.0.0
+  __TEXT.__text: 0x9e478
   __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0xe114
-  __TEXT.__const: 0xa48
+  __TEXT.__objc_methlist: 0xe07c
+  __TEXT.__const: 0xa58
   __TEXT.__gcc_except_tab: 0x97c
-  __TEXT.__cstring: 0xa37e
+  __TEXT.__cstring: 0xa560
   __TEXT.__dlopen_cstrs: 0x3cc
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x4354
-  __TEXT.__unwind_info: 0x2f28
+  __TEXT.__oslogstring: 0x43c2
+  __TEXT.__unwind_info: 0x2f18
   __TEXT.__objc_classname: 0x3db9
-  __TEXT.__objc_methname: 0x238d3
+  __TEXT.__objc_methname: 0x2364d
   __TEXT.__objc_methtype: 0x6027
-  __TEXT.__objc_stubs: 0x168a0
+  __TEXT.__objc_stubs: 0x16840
   __DATA_CONST.__got: 0x1020
   __DATA_CONST.__const: 0x2bd8
   __DATA_CONST.__objc_classlist: 0x900
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x4b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7998
+  __DATA_CONST.__objc_selrefs: 0x7930
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x5c0
   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0xb08
   __AUTH_CONST.__const: 0x960
-  __AUTH_CONST.__cfstring: 0x9d00
-  __AUTH_CONST.__objc_const: 0x2c900
+  __AUTH_CONST.__cfstring: 0x9da0
+  __AUTH_CONST.__objc_const: 0x2c810
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x4b00
-  __DATA.__objc_ivar: 0xcd8
+  __DATA.__objc_ivar: 0xcc4
   __DATA.__data: 0x38c8
   __DATA.__bss: 0x3c8
   __DATA_DIRTY.__objc_data: 0xf00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 554FC49D-510B-38F3-B1E3-6EC5796A8465
-  Functions: 4576
-  Symbols:   17333
-  CStrings:  9419
+  UUID: BEA06CD0-091B-3CE8-8388-6A04939CF598
+  Functions: 4561
+  Symbols:   17295
+  CStrings:  9408
 
Symbols:
+ _objc_msgSend$clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:
+ _objc_msgSend$clientRequestToAcknowledgeDidFinishAnimatingFor:withFileStackIcon:
- -[SBUIPasscodeBiometricAuthenticationView _leadingForFaceIDReason]
- -[SBUIPasscodeBiometricAuthenticationView _noteContentSizeCategoryDidChange]
- -[SBUIPasscodeBiometricAuthenticationView _setFaceIDReason2:]
- -[SBUIPasscodeBiometricAuthenticationView _setFaceIDReason:]
- -[SBUIPasscodeBiometricAuthenticationView _setFaceIDReasonLine2:]
- -[SBUIPasscodeBiometricAuthenticationView faceIDLabelAndReasonLayoutGuide]
- -[SBUIPasscodeBiometricAuthenticationView faceIDLabelFaceIDReasonBaselineConstraint]
- -[SBUIPasscodeBiometricAuthenticationView faceIDLabel]
- -[SBUIPasscodeBiometricAuthenticationView faceIDReasonLine2]
- -[SBUIPasscodeBiometricAuthenticationView faceIDReason]
- -[SBUIPasscodeBiometricAuthenticationView setFaceIDLabel:]
- -[SBUIPasscodeBiometricAuthenticationView setFaceIDLabelAndReasonLayoutGuide:]
- -[SBUIPasscodeBiometricAuthenticationView setFaceIDLabelFaceIDReasonBaselineConstraint:]
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDLabel
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDLabelAndReasonLayoutGuide
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDLabelFaceIDReasonBaselineConstraint
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDReason
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDReasonLine2
- ___102-[SBUISFloatingDockRemoteContentHostComponent fetchIconThumbnailWithSessionID:forIcon:url:completion:]_block_invoke
- ___124-[SBUISFloatingDockRemoteContentHostComponent moveDocumentWithSessionID:securityURLWrappers:toFileStackIcon:url:completion:]_block_invoke
- _objc_msgSend$_leadingForFaceIDReason
- _objc_msgSend$_setFaceIDReason:
- _objc_msgSend$_setFaceIDReasonLine2:
- _objc_msgSend$addAction:
- _objc_msgSend$clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:
CStrings:
+ "Host scene is active %{public}d at document move."
+ "Host scene is active %{public}d at thumbnail fetch."
+ "Host scene is active %{public}d."
+ "SBUISFloatingDockFileStackRequestAcknowledgeFinishClosingAnimationFromClient"
+ "SBUISFloatingDockFileStackRequestAcknowledgeFinishOpeningAnimationFromClient"
+ "SBUISFloatingDockFileStackRequestCloseWithoutAnimationFromHost"
+ "SBUISFloatingDockFileStackRequestCompletionFromClient"
+ "SBUISFloatingDockFileStackRequestFinishDownloadAnimationDidEndFromHost"
+ "SBUISFloatingDockFileStackRequestFinishDownloadAnimationWillBeginFromHost"
+ "SBUISFloatingDockFileStackRequestIconAddedFromClient"
+ "SBUISFloatingDockFileStackRequestIconRemovedFromClient"
+ "SBUISFloatingDockFileStackRequestOpenWithoutAnimationFromHost"
+ "Unknown request"
+ "clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:"
+ "clientRequestToAcknowledgeDidFinishAnimatingFor:withFileStackIcon:"
- "FACE_ID_LABEL"
- "FACE_ID_REASON_LINE_1"
- "FACE_ID_REASON_LINE_2"
- "Host scene is active %d."
- "T@\"NSLayoutConstraint\",&,N,V_faceIDLabelFaceIDReasonBaselineConstraint"
- "T@\"NSString\",C,N,S_setFaceIDReason2:,V_faceIDReasonLine2"
- "T@\"NSString\",C,N,S_setFaceIDReason:,V_faceIDReason"
- "T@\"UILabel\",&,N,V_faceIDLabel"
- "T@\"UILayoutGuide\",&,N,V_faceIDLabelAndReasonLayoutGuide"
- "UNLOCKING_WITH_WATCH_LABEL"
- "UNLOCKING_WITH_WATCH_REASON_LINE_1"
- "_faceIDLabel"
- "_faceIDLabelAndReasonLayoutGuide"
- "_faceIDLabelFaceIDReasonBaselineConstraint"
- "_faceIDReason"
- "_faceIDReasonLine2"
- "_leadingForFaceIDReason"
- "_noteContentSizeCategoryDidChange"
- "_setFaceIDReason2:"
- "_setFaceIDReason:"
- "_setFaceIDReasonLine2:"
- "addAction:"
- "clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:"
- "faceIDLabel"
- "faceIDLabelAndReasonLayoutGuide"
- "faceIDLabelFaceIDReasonBaselineConstraint"
- "faceIDReason"
- "faceIDReasonLine2"
- "setFaceIDLabel:"
- "setFaceIDLabelAndReasonLayoutGuide:"
- "setFaceIDLabelFaceIDReasonBaselineConstraint:"

```
