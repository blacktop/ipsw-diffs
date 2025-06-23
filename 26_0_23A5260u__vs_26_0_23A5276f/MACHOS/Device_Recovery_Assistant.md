## Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

-74.0.0.0.2
-  __TEXT.__text: 0xc61c
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x2d60
-  __TEXT.__objc_methlist: 0x1a00
+82.0.0.502.1
+  __TEXT.__text: 0xce64
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x2f60
+  __TEXT.__objc_methlist: 0x1ab8
+  __TEXT.__cstring: 0x1925
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x1842
-  __TEXT.__objc_methname: 0x5000
-  __TEXT.__oslogstring: 0x1621
-  __TEXT.__objc_classname: 0x3d3
-  __TEXT.__objc_methtype: 0x1f9c
+  __TEXT.__objc_methname: 0x5209
+  __TEXT.__oslogstring: 0x16ce
+  __TEXT.__objc_classname: 0x3eb
+  __TEXT.__objc_methtype: 0x1fd0
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x3a8
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x608
-  __DATA_CONST.__cfstring: 0xa80
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__unwind_info: 0x3b0
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x5f0
+  __DATA_CONST.__cfstring: 0xb40
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA.__objc_const: 0x2f38
-  __DATA.__objc_selrefs: 0x1380
-  __DATA.__objc_ivar: 0xc8
-  __DATA.__objc_data: 0x5f0
+  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA.__objc_const: 0x3098
+  __DATA.__objc_selrefs: 0x1428
+  __DATA.__objc_ivar: 0xd8
+  __DATA.__objc_data: 0x640
   __DATA.__data: 0x918
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54670D25-FBD1-30B9-B7F0-61573AB7AFEA
-  Functions: 360
-  Symbols:   208
-  CStrings:  1349
+  UUID: C890596F-B517-3686-A7D6-AA2BE12F0316
+  Functions: 375
+  Symbols:   213
+  CStrings:  1400
 
Symbols:
+ _CGAffineTransformMakeScale
+ _MGCopyAnswer
+ _OBJC_CLASS_$_CIFilter
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _kIOMainPortDefault
+ _objc_enumerationMutation
- _kIOMasterPortDefault
CStrings:
+ "%{public}s: Info button pushed on done view of device."
+ "%{public}s: Info button pushed on failure view of device."
+ "%{public}s: Reboot button pushed on failure view of device."
+ "-[DoneViewController _didTapInfoButton:]"
+ "-[FailureViewController _didTapInfoButton:]"
+ "@\"CoreTelephonyClient\""
+ "@\"UIImageView\""
+ "@28@0:8@16B24"
+ "CICode128BarcodeGenerator"
+ "CIQRCodeGenerator"
+ "DetailsView"
+ "DetailsViewController"
+ "IMEI"
+ "SerialNumber"
+ "T@\"CoreTelephonyClient\",&,V_telephony"
+ "T@\"UIImageView\",&,V_qrCodeView"
+ "T@\"UILabel\",&,V_imeiLabel"
+ "T@\"UILabel\",&,V_serialNumberLabel"
+ "_didTapInfoButton:"
+ "_generateBarcode:showAsQRCode:"
+ "_imeiLabel"
+ "_qrCodeView"
+ "_serialNumberLabel"
+ "_telephony"
+ "copyMobileEquipmentInfo:"
+ "countByEnumeratingWithState:objects:count:"
+ "dataUsingEncoding:"
+ "filterWithName:"
+ "imageByApplyingTransform:"
+ "imeiLabel"
+ "info.circle"
+ "initWithCIImage:"
+ "initWithQueue:"
+ "inputMessage"
+ "meInfoList"
+ "outputImage"
+ "qrCodeView"
+ "serialNumberLabel"
+ "setImage:"
+ "setImeiLabel:"
+ "setQrCodeView:"
+ "setSerialNumberLabel:"
+ "setTelephony:"
+ "simplePasscodeType"
+ "telephony"
+ "v24@?0@\"CTMobileEquipmentInfoList\"8@\"NSError\"16"
- "unlockScreenTypeWithOutSimplePasscodeType:"

```
