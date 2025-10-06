## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-526.9.0.0.0
-  __TEXT.__text: 0x1b5ec
+526.15.0.0.0
+  __TEXT.__text: 0x1b64c
   __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_methlist: 0x2d5c
   __TEXT.__const: 0x1f0

   __TEXT.__gcc_except_tab: 0x420
   __TEXT.__unwind_info: 0x960
   __TEXT.__objc_classname: 0xefa
-  __TEXT.__objc_methname: 0x5b16
+  __TEXT.__objc_methname: 0x5af1
   __TEXT.__objc_methtype: 0x1339
-  __TEXT.__objc_stubs: 0x3d40
+  __TEXT.__objc_stubs: 0x3d60
   __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__objc_classlist: 0x280

   __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x4e0
   __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0xef28
+  __AUTH_CONST.__objc_const: 0xef08
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x320
+  __DATA.__objc_ivar: 0x31c
   __DATA.__data: 0xfc8
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3D38911-E1C8-323D-B1F0-3C47D91DEF33
+  UUID: E866A037-3FE5-365C-914A-8022A01F7D4C
   Functions: 932
   Symbols:   4058
-  CStrings:  1664
+  CStrings:  1663
 
Symbols:
+ _objc_msgSend$description
- _OBJC_IVAR_$_CRSUIMutableClimateOverlaySceneSettings._primaryDockFrame
Functions:
~ -[CRSUIMutableClimateOverlaySceneSettings hasPhysicalControlBars] -> -[CRSUIMutableClimateOverlaySceneSettings primaryDockFrame] : 88 -> 120
~ -[CRSUIMutableClimateOverlaySceneSettings setHasPhysicalControlBars:] -> -[CRSUIMutableClimateOverlaySceneSettings hasPhysicalControlBars] : 120 -> 88
~ -[CRSUIMutableClimateOverlaySceneSettings persistentElements] -> -[CRSUIMutableClimateOverlaySceneSettings setHasPhysicalControlBars:] : 84 -> 120
~ -[CRSUIMutableClimateOverlaySceneSettings setPersistentElements:] -> -[CRSUIMutableClimateOverlaySceneSettings persistentElements] : 124 -> 84
~ -[CRSUIMutableClimateOverlaySceneSettings setPrimaryDockFrame:] -> -[CRSUIMutableClimateOverlaySceneSettings setPersistentElements:] : 160 -> 124
~ -[CRSUIMutableClimateOverlaySceneSettings copyWithZone:] -> -[CRSUIMutableClimateOverlaySceneSettings setSecondaryDockFrame:] : 64 -> 160
~ -[CRSUIMutableClimateOverlaySceneSettings primaryDockFrame] -> -[CRSUIMutableClimateOverlaySceneSettings copyWithZone:] : 24 -> 64
CStrings:
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_primaryDockFrame"
- "_primaryDockFrame"

```
