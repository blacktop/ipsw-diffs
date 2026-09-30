## AccessibilityKit

> `/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityKit.framework/Versions/A/AccessibilityKit`

```diff

-387.5.2.0.0
-  __TEXT.__text: 0x422fc
+387.7.3.0.0
+  __TEXT.__text: 0x419c8
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x2f08
+  __TEXT.__objc_methlist: 0x322c
   __TEXT.__const: 0x1f9
-  __TEXT.__gcc_except_tab: 0x4cc
+  __TEXT.__gcc_except_tab: 0x4d4
   __TEXT.__cstring: 0x2997
   __TEXT.__ustring: 0x3c
   __TEXT.__dlopen_cstrs: 0x72
   __TEXT.__oslogstring: 0x808
-  __TEXT.__unwind_info: 0xee0
+  __TEXT.__unwind_info: 0xec0
   __TEXT.__objc_classname: 0x532
   __TEXT.__objc_methname: 0xb675
   __TEXT.__objc_methtype: 0x1463

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2690
+  __DATA_CONST.__objc_selrefs: 0x2750
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x10d0
   __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x6730
+  __AUTH_CONST.__objc_const: 0x6178
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd70

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BAC136B1-0365-3AD5-B2C4-4CCCCE233824
-  Functions: 1451
-  Symbols:   3563
+  UUID: 8F3367D3-49A3-32B8-BC41-BAC48BC66E14
+  Functions: 1561
+  Symbols:   3677
   CStrings:  2443
 
Symbols:
+ +[AXKResourceManager shared].cold.1
+ +[AXKTextElementEditTracker _wordTerminationCharSet].cold.1
+ +[AXKTextElementEditTracker isEditableTextUIElement:].cold.1
+ -[AXKElementController visibleBounds].cold.1
+ -[AXKWorkspaceManager _applicationControllerClassForApplicationElement:].cold.1
+ -[NSString(AXKExtensions) axk_containsAttachmentCharSet].cold.1
+ -[NSString(AXKExtensions) axk_isWordCompletionCharacter].cold.1
+ ACMContextGetExternalForm.cold.1
+ AXKFullKeyboardAccessAvailableCommands.cold.1
+ _AXKSharedClassRegistrar.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ updateLogLevelFromKext.cold.1
- __isNullOrEqualMem2
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"

```
