## AuthenticationServicesUI

> `/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI`

```diff

-7617.2.4.10.8
-  __TEXT.__text: 0x48d0
-  __TEXT.__auth_stubs: 0x780
+7618.1.15.10.11
+  __TEXT.__text: 0x4b14
+  __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x1bc
+  __TEXT.__objc_methlist: 0x1a4
   __TEXT.__objc_classname: 0x126
-  __TEXT.__objc_methname: 0x182c
+  __TEXT.__objc_methname: 0x1840
   __TEXT.__objc_methtype: 0xeb9
-  __TEXT.__cstring: 0x3e8
+  __TEXT.__cstring: 0x638
   __TEXT.__const: 0x94
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__oslogstring: 0x15a
   __TEXT.__constg_swiftt: 0x128
-  __TEXT.__swift5_typeref: 0x100
+  __TEXT.__swift5_typeref: 0x102
   __TEXT.__swift5_reflstr: 0x43
   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__unwind_info: 0x194
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x13e0
-  __DATA.__objc_selrefs: 0x2c8
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x88
-  __DATA.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x13c8
+  __DATA.__objc_selrefs: 0x2b8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x288
   __DATA.__data: 0x538

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI
+  - /System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI
   - /System/Library/PrivateFrameworks/SafariCore.framework/SafariCore
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BA23A8BA-9FA5-3954-8835-9627BBFAC19A
+  UUID: 5FD8B3A6-D339-3E95-97C9-34E9E2ADE6E9
   Functions: 104
-  Symbols:   193
-  CStrings:  342
+  Symbols:   201
+  CStrings:  355
 
Symbols:
+ _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyFyXl_Ts5
+ _$sSa12_endMutationyyFyXl_Ts5
+ _$sSa16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFyXl_Ts5
+ _$sSa37_appendElementAssumeUniqueAndCapacity_03newB0ySi_xntFyXl_Ts5
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _OBJC_CLASS_$_PMAuthorizationViewController
+ _objc_retain_x9
+ _swift_beginAccess
+ _swift_endAccess
- _OBJC_CLASS_$_ASAuthorizationViewController
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "@\"PMAuthorizationViewController\""
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "PMAuthorizationViewControllerDelegate"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIWindow\",?,&,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
+ "v24@0:8@\"PMAuthorizationViewController\"16"
+ "v32@0:8@\"PMAuthorizationViewController\"16@?<v@?@\"ASCAuthorizationPresentationContext\"@\"NSError\">24"
+ "v40@0:8@\"PMAuthorizationViewController\"16@\"<ASCCredentialProtocol>\"24@\"NSError\"32"
+ "v40@0:8@\"PMAuthorizationViewController\"16@\"NSString\"24@?<v@?@\"<ASCCredentialProtocol>\"@\"NSError\">32"
+ "v48@0:8@\"PMAuthorizationViewController\"16@\"<ASCLoginChoiceProtocol>\"24@\"LAContext\"32@?<v@?@\"<ASCCredentialProtocol>\"@\"NSError\">40"
+ "windows"
- "@\"ASAuthorizationViewController\""
- "ASAuthorizationViewControllerDelegate"
- "T@\"UIWindow\",&,N"
- "T@\"UIWindow\",N,&,Vwindow"
- "v24@0:8@\"ASAuthorizationViewController\"16"
- "v32@0:8@\"ASAuthorizationViewController\"16@?<v@?@\"ASCAuthorizationPresentationContext\"@\"NSError\">24"
- "v40@0:8@\"ASAuthorizationViewController\"16@\"<ASCCredentialProtocol>\"24@\"NSError\"32"
- "v40@0:8@\"ASAuthorizationViewController\"16@\"NSString\"24@?<v@?@\"<ASCCredentialProtocol>\"@\"NSError\">32"
- "v48@0:8@\"ASAuthorizationViewController\"16@\"<ASCLoginChoiceProtocol>\"24@\"LAContext\"32@?<v@?@\"<ASCCredentialProtocol>\"@\"NSError\">40"

```
