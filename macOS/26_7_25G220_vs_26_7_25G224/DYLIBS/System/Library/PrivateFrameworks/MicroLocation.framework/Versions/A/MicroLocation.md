## MicroLocation

> `/System/Library/PrivateFrameworks/MicroLocation.framework/Versions/A/MicroLocation`

```diff

 62.0.3.0.0
-  __TEXT.__text: 0x1bd94
+  __TEXT.__text: 0x1b0a8
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x228c
-  __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x29b4
+  __TEXT.__objc_methlist: 0x218c
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x2820
   __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__oslogstring: 0xbef
-  __TEXT.__unwind_info: 0x868
-  __TEXT.__objc_classname: 0x2f1
-  __TEXT.__objc_methname: 0x48b6
-  __TEXT.__objc_methtype: 0xaac
-  __TEXT.__objc_stubs: 0x2e00
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x438
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__oslogstring: 0xb46
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__objc_classname: 0x2e1
+  __TEXT.__objc_methname: 0x4660
+  __TEXT.__objc_methtype: 0xa2b
+  __TEXT.__objc_stubs: 0x2d00
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe90
+  __DATA_CONST.__objc_selrefs: 0xe38
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0x2e00
-  __AUTH_CONST.__objc_const: 0x3490
+  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__objc_const: 0x32c0
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1e4
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x240
-  __DATA_DIRTY.__objc_data: 0x870
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 731
-  Symbols:   1771
-  CStrings:  1281
+  Functions: 711
+  Symbols:   1725
+  CStrings:  1228
 
Symbols:
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table143
+ GCC_except_table21
+ GCC_except_table27
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table47
+ GCC_except_table74
- +[ULConnection fetchEnvironmentDescriptionWithOptions:reply:]
- +[ULSpatialObject coarseOrientationToString:]
- +[ULSpatialObject supportsSecureCoding]
- -[ULSpatialObject .cxx_destruct]
- -[ULSpatialObject coarseObjectOrientation]
- -[ULSpatialObject confidence]
- -[ULSpatialObject copyWithZone:]
- -[ULSpatialObject description]
- -[ULSpatialObject encodeWithCoder:]
- -[ULSpatialObject hash]
- -[ULSpatialObject initWithCoder:]
- -[ULSpatialObject initWithObjectName:objectAngle:objectAngleUncertainty:coarseObjectOrientation:]
- -[ULSpatialObject initWithObjectName:objectAngle:objectAngleUncertainty:coarseObjectOrientation:confidence:]
- -[ULSpatialObject isEqual:]
- -[ULSpatialObject isObjectAngleValid]
- -[ULSpatialObject objectAngleUncertainty]
- -[ULSpatialObject objectAngle]
- -[ULSpatialObject objectName]
- GCC_except_table118
- GCC_except_table120
- GCC_except_table146
- GCC_except_table24
- GCC_except_table30
- GCC_except_table34
- GCC_except_table36
- GCC_except_table50
- GCC_except_table77
- OBJC_IVAR_$_ULSpatialObject._coarseObjectOrientation
- OBJC_IVAR_$_ULSpatialObject._confidence
- OBJC_IVAR_$_ULSpatialObject._objectAngle
- OBJC_IVAR_$_ULSpatialObject._objectAngleUncertainty
- OBJC_IVAR_$_ULSpatialObject._objectName
- _OBJC_CLASS_$_ULSpatialObject
- _OBJC_METACLASS_$_ULSpatialObject
- _ULSpatialObjectMaxAngleDegree
- _ULSpatialObjectMinAngleDegree
- _ULSpatialObjectMinAngleUncNotInclusive
- __61+[ULConnection fetchEnvironmentDescriptionWithOptions:reply:]_block_invoke
- __OBJC_$_CLASS_METHODS_ULSpatialObject
- __OBJC_$_CLASS_PROP_LIST_ULSpatialObject
- __OBJC_$_INSTANCE_METHODS_ULSpatialObject
- __OBJC_$_INSTANCE_VARIABLES_ULSpatialObject
- __OBJC_$_PROP_LIST_ULSpatialObject
- __OBJC_CLASS_PROTOCOLS_$_ULSpatialObject
- __OBJC_CLASS_RO_$_ULSpatialObject
- __OBJC_METACLASS_RO_$_ULSpatialObject
- ___61+[ULConnection fetchEnvironmentDescriptionWithOptions:reply:]_block_invoke
- _objc_msgSend$coarseObjectOrientation
- _objc_msgSend$confidence
- _objc_msgSend$createAccessibilitySessionWithOptions:reply:
- _objc_msgSend$doubleValue
- _objc_msgSend$initWithObjectName:objectAngle:objectAngleUncertainty:coarseObjectOrientation:confidence:
- _objc_msgSend$objectAngle
- _objc_msgSend$objectAngleUncertainty
- _objc_msgSend$objectName
CStrings:
- ",coarseObjectOrientation: %@"
- ",confidence: %.3f"
- ",objectAngle: %.2f"
- ",objectAngleUncertainty: %.2f"
- "<%@:"
- "@48@0:8@16d24d32q40"
- "@56@0:8@16d24d32q40d48"
- "Back"
- "Back Left"
- "Back Right"
- "Creating an accessibility session, in dispatch_async"
- "Creating session, identifier: %@, error:%@"
- "Far Back"
- "Far Back Left"
- "Far Back Right"
- "Far Front"
- "Far Front Left"
- "Far Front Right"
- "Front"
- "Left"
- "Near Back"
- "Near Back Left"
- "Near Back Right"
- "Near Front"
- "Near Front Left"
- "Near Front Right"
- "Right"
- "T@\"NSString\",R,N,V_objectName"
- "Td,R,N,V_confidence"
- "Td,R,N,V_objectAngle"
- "Td,R,N,V_objectAngleUncertainty"
- "Tq,R,N,V_coarseObjectOrientation"
- "ULSpatialObject"
- "_coarseObjectOrientation"
- "_objectAngle"
- "_objectAngleUncertainty"
- "_objectName"
- "coarseObjectOrientation"
- "coarseOrientationToString:"
- "createAccessibilitySessionWithOptions:reply:"
- "d"
- "d16@0:8"
- "doubleValue"
- "fetchEnvironmentDescriptionWithOptions,creating an accessibility session"
- "fetchEnvironmentDescriptionWithOptions:reply:"
- "initWithObjectName:objectAngle:objectAngleUncertainty:coarseObjectOrientation:"
- "initWithObjectName:objectAngle:objectAngleUncertainty:coarseObjectOrientation:confidence:"
- "isObjectAngleValid"
- "objectAngle"
- "objectAngleUncertainty"
- "objectName"
- "objectName: %@"
- "v32@0:8@\"ULAccessibilitySessionFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
```
