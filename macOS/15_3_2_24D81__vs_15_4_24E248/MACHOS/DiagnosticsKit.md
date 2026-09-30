## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/Versions/A/DiagnosticsKit`

```diff

-63.0.0.0.0
-  __TEXT.__text: 0x1cc80
+63.100.1.0.0
+  __TEXT.__text: 0x1cc30
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x20a8
+  __TEXT.__objc_methlist: 0x285c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x1928
+  __TEXT.__cstring: 0x1952
   __TEXT.__gcc_except_tab: 0x774
   __TEXT.__oslogstring: 0x10d3
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__unwind_info: 0x808
   __TEXT.__objc_classname: 0x5f9
-  __TEXT.__objc_methname: 0x4afe
-  __TEXT.__objc_methtype: 0xec5
+  __TEXT.__objc_methname: 0x4b28
+  __TEXT.__objc_methtype: 0xed4
   __TEXT.__objc_stubs: 0x36e0
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0x258

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10c8
+  __DATA_CONST.__objc_selrefs: 0x1168
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xf8
   __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x7b0
   __AUTH_CONST.__cfstring: 0xcc0
-  __AUTH_CONST.__objc_const: 0x53d8
+  __AUTH_CONST.__objc_const: 0x4690
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH.__objc_data: 0xc80
   __DATA.__objc_ivar: 0x248

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BCA218CF-9556-3D94-B57B-582BD5FC8EAF
-  Functions: 807
-  Symbols:   2194
+  UUID: 6166305C-677B-3857-9E4D-E81653D0822E
+  Functions: 821
+  Symbols:   2208
   CStrings:  1438
 
Symbols:
+ +[DKDiagnosticContext _extensionAuxiliaryHostProtocol].cold.1
+ +[DKDiagnosticContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[DKDiagnosticHostContext _extensionAuxiliaryHostProtocol].cold.1
+ +[DKDiagnosticHostContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[DKReportHostContext _extensionAuxiliaryHostProtocol].cold.1
+ +[DKReportHostContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[DKReporterContext _extensionAuxiliaryHostProtocol].cold.1
+ +[DKReporterContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[DKUtilities _sharedParsingFailedError].cold.1
+ +[DKUtilities acceptableDecoderClasses].cold.1
+ -[DKAssetUploadItem _decoderClasses].cold.1
+ -[DKAssetUploadItems _decoderClasses].cold.1
+ -[DKDiagnosticContext displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:]
+ -[DKDiagnosticContext remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:]
+ -[DKDiagnosticContextMock displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:]
+ -[DKDiagnosticHostContext remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:]
+ -[DKDiagnosticManager displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:]
+ -[DKDiagnosticParameters _decoderClasses].cold.1
+ DiagnosticsKitLogHandleForCategory.cold.1
+ GCC_except_table47
+ _objc_msgSend$displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:
+ _objc_msgSend$remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:
- -[DKDiagnosticContext displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:]
- -[DKDiagnosticContext remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:]
- -[DKDiagnosticContextMock displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:]
- -[DKDiagnosticHostContext remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:]
- -[DKDiagnosticManager displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:]
- GCC_except_table48
- _objc_msgSend$displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:
- _objc_msgSend$remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:
CStrings:
+ "-[DKDiagnosticContext displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:]"
+ "-[DKDiagnosticContextMock displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:]"
+ "displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:"
+ "remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:"
+ "v84@0:8@\"NSArray\"16i24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@\"NSArray\"68@?<v@?@\"NSString\"@\"NSError\">76"
+ "v84@0:8@16i24@28@36@44@52@60@68@?76"
- "-[DKDiagnosticContext displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:]"
- "-[DKDiagnosticContextMock displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:]"
- "displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:"
- "remoteHostDisplayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:"
- "v76@0:8@\"NSArray\"16i24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@?<v@?@\"NSString\"@\"NSError\">68"
- "v76@0:8@16i24@28@36@44@52@60@?68"

```
