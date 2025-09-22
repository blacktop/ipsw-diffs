## AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

-494.4.9.0.0
-  __TEXT.__text: 0x625c
+494.4.12.0.0
+  __TEXT.__text: 0x7010
   __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__objc_stubs: 0x12a0
+  __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__cstring: 0x46c
-  __TEXT.__objc_methname: 0x15b5
-  __TEXT.__oslogstring: 0x1143
+  __TEXT.__objc_methname: 0x171d
+  __TEXT.__oslogstring: 0x12d5
   __TEXT.__objc_classname: 0xf0
-  __TEXT.__objc_methtype: 0x64a
-  __TEXT.__unwind_info: 0x1bc
+  __TEXT.__objc_methtype: 0x65b
+  __TEXT.__unwind_info: 0x1d4
   __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x388
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x840
-  __DATA.__objc_selrefs: 0x4c8
-  __DATA.__objc_classrefs: 0xe0
+  __DATA.__objc_const: 0x860
+  __DATA.__objc_selrefs: 0x520
+  __DATA.__objc_classrefs: 0xf0
   __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BEEB1EC2-D4E6-3ECE-9689-A1B46D0D81DF
-  Functions: 123
-  Symbols:   124
-  CStrings:  402
+  UUID: 5B720E06-55D9-375B-8EC1-4C2E265384DA
+  Functions: 150
+  Symbols:   126
+  CStrings:  421
 
Symbols:
+ _OBJC_CLASS_$_AAUIDTOHelper
+ _OBJC_CLASS_$_AKBiometricRatchetController
CStrings:
+ "\t"
+ "@\"AAUIDTOHelper\""
+ "DTO disabled, proceeding with usual flow without auth"
+ "DTO enabled, IdMS says RC add is allowed, proceeding to ratchet auth"
+ "IdMS says RC add is allowed on this device, proceeding to check if DTO is enabled"
+ "IdMS says RC add is not allowed on weak device, proceeding to show error alert"
+ "Ratchet auth returned with success: %d, error: %@,"
+ "_displayCustodianAddNotAllowedAlert"
+ "_displayRatchetGenericErrorAlert"
+ "accounts"
+ "appleAccount found nil, returning without setting up the custodian"
+ "dtoHelper"
+ "initWithDTOController:"
+ "isDTOGatingEnabled"
+ "makeCustodianAddOpNotAllowedAlert"
+ "makeGenericRatchetFailedAlert"
+ "makeRatchetContextWithPresentationContext:DTOContextType:"
+ "presentingViewController"
+ "shouldAllowOpForContext:completion:"
+ "shouldGateUsingRatchetForAltDSID:completion:"
- "\b"

```
