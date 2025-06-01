## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-11.1.9.0.0
-  __TEXT.__text: 0x46f64
+11.2.3.0.0
+  __TEXT.__text: 0x4a5f0
   __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x4a0c
+  __TEXT.__objc_methlist: 0x4e34
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x5571
-  __TEXT.__gcc_except_tab: 0x1c88
+  __TEXT.__cstring: 0x5763
+  __TEXT.__gcc_except_tab: 0x1d28
   __TEXT.__oslogstring: 0x1bfa
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x1834
+  __TEXT.__unwind_info: 0x1928
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1274
-  __TEXT.__objc_methname: 0x6b6c
-  __TEXT.__objc_methtype: 0x145c
-  __TEXT.__objc_stubs: 0x4340
+  __TEXT.__objc_classname: 0x1379
+  __TEXT.__objc_methname: 0x6c80
+  __TEXT.__objc_methtype: 0x1484
+  __TEXT.__objc_stubs: 0x43c0
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x1328
-  __DATA_CONST.__objc_classlist: 0x368
+  __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbb60
-  __DATA_CONST.__objc_selrefs: 0x1660
+  __DATA_CONST.__objc_const: 0xc0f0
+  __DATA_CONST.__objc_selrefs: 0x1680
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__cfstring: 0x5da0
-  __AUTH_CONST.__objc_const: 0x36c8
+  __AUTH_CONST.__cfstring: 0x5fa0
+  __AUTH_CONST.__objc_const: 0x3a28
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__const: 0x4a8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x758
-  __AUTH.__objc_data: 0x1950
+  __AUTH.__objc_data: 0x1b30
   __AUTH.__data: 0xdb8
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x378
-  __DATA.__objc_superrefs: 0x340
-  __DATA.__objc_ivar: 0x580
+  __DATA.__objc_classrefs: 0x3a0
+  __DATA.__objc_superrefs: 0x370
+  __DATA.__objc_ivar: 0x5c0
   __DATA.__data: 0xb40
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB0CC2E8-EE34-3875-A2B9-D6F0DE4381E4
-  Functions: 1812
-  Symbols:   6801
-  CStrings:  3386
+  UUID: 562872E5-797C-3AF1-BF56-E595D921622F
+  Functions: 1893
+  Symbols:   7055
+  CStrings:  3437
 
Symbols:
+ +[GCGenericDeviceDataElementExistsExpressionModel description]
+ +[GCGenericDeviceDataElementExistsExpressionModel supportsSecureCoding]
+ +[GCGenericDeviceDataElementExistsExpressionModelBuilder modelClass]
+ +[GCGenericDeviceDriverPropertiesModel description]
+ +[GCGenericDeviceDriverPropertiesModel supportsSecureCoding]
+ +[GCGenericDeviceDriverPropertiesModel(Serialization) modelWithDictionaryRepresentation:error:]
+ +[GCGenericDeviceDriverPropertiesModelBuilder modelClass]
+ +[GCGenericDeviceDriverPropertyModel description]
+ +[GCGenericDeviceDriverPropertyModel supportsSecureCoding]
+ +[GCGenericDeviceDriverPropertyModel(Serialization) modelWithDictionaryRepresentation:error:]
+ +[GCGenericDeviceDriverPropertyModelBuilder modelClass]
+ -[GCGenericDeviceDataElementExistsExpressionModel .cxx_destruct]
+ -[GCGenericDeviceDataElementExistsExpressionModel debugDescription]
+ -[GCGenericDeviceDataElementExistsExpressionModel description]
+ -[GCGenericDeviceDataElementExistsExpressionModel elementIdentifier]
+ -[GCGenericDeviceDataElementExistsExpressionModel encodeWithCoder:]
+ -[GCGenericDeviceDataElementExistsExpressionModel falseExpression]
+ -[GCGenericDeviceDataElementExistsExpressionModel initWithCoder:]
+ -[GCGenericDeviceDataElementExistsExpressionModel isEqual:]
+ -[GCGenericDeviceDataElementExistsExpressionModel redactedDescription]
+ -[GCGenericDeviceDataElementExistsExpressionModel trueExpression]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder .cxx_destruct]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder build]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder elementIdentifier]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder falseExpression]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder initializeWithModel:]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder reset]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder setElementIdentifier:]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder setFalseExpression:]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder setTrueExpression:]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder trueExpression]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder(Serialization) initWithDictionaryRepresentation:error:]
+ -[GCGenericDeviceDriverModel properties]
+ -[GCGenericDeviceDriverModelBuilder properties]
+ -[GCGenericDeviceDriverModelBuilder setProperties:]
+ -[GCGenericDeviceDriverPropertiesModel .cxx_destruct]
+ -[GCGenericDeviceDriverPropertiesModel copyWithZone:]
+ -[GCGenericDeviceDriverPropertiesModel debugDescription]
+ -[GCGenericDeviceDriverPropertiesModel encodeWithCoder:]
+ -[GCGenericDeviceDriverPropertiesModel hash]
+ -[GCGenericDeviceDriverPropertiesModel initWithCoder:]
+ -[GCGenericDeviceDriverPropertiesModel init]
+ -[GCGenericDeviceDriverPropertiesModel isEqual:]
+ -[GCGenericDeviceDriverPropertiesModel properties]
+ -[GCGenericDeviceDriverPropertiesModelBuilder .cxx_destruct]
+ -[GCGenericDeviceDriverPropertiesModelBuilder build]
+ -[GCGenericDeviceDriverPropertiesModelBuilder hash]
+ -[GCGenericDeviceDriverPropertiesModelBuilder init]
+ -[GCGenericDeviceDriverPropertiesModelBuilder initializeWithModel:]
+ -[GCGenericDeviceDriverPropertiesModelBuilder isEqual:]
+ -[GCGenericDeviceDriverPropertiesModelBuilder properties]
+ -[GCGenericDeviceDriverPropertiesModelBuilder reset]
+ -[GCGenericDeviceDriverPropertiesModelBuilder setProperties:]
+ -[GCGenericDeviceDriverPropertyModel .cxx_destruct]
+ -[GCGenericDeviceDriverPropertyModel copyWithZone:]
+ -[GCGenericDeviceDriverPropertyModel debugDescription]
+ -[GCGenericDeviceDriverPropertyModel description]
+ -[GCGenericDeviceDriverPropertyModel encodeWithCoder:]
+ -[GCGenericDeviceDriverPropertyModel hash]
+ -[GCGenericDeviceDriverPropertyModel initWithCoder:]
+ -[GCGenericDeviceDriverPropertyModel init]
+ -[GCGenericDeviceDriverPropertyModel isEqual:]
+ -[GCGenericDeviceDriverPropertyModel name]
+ -[GCGenericDeviceDriverPropertyModel valueExpression]
+ -[GCGenericDeviceDriverPropertyModelBuilder .cxx_destruct]
+ -[GCGenericDeviceDriverPropertyModelBuilder build]
+ -[GCGenericDeviceDriverPropertyModelBuilder hash]
+ -[GCGenericDeviceDriverPropertyModelBuilder init]
+ -[GCGenericDeviceDriverPropertyModelBuilder initializeWithModel:]
+ -[GCGenericDeviceDriverPropertyModelBuilder isEqual:]
+ -[GCGenericDeviceDriverPropertyModelBuilder name]
+ -[GCGenericDeviceDriverPropertyModelBuilder reset]
+ -[GCGenericDeviceDriverPropertyModelBuilder setName:]
+ -[GCGenericDeviceDriverPropertyModelBuilder setValueExpression:]
+ -[GCGenericDeviceDriverPropertyModelBuilder valueExpression]
+ -[GCGenericDeviceElementModel optional]
+ -[GCGenericDeviceElementModelBuilder optional]
+ -[GCGenericDeviceElementModelBuilder setOptional:]
+ _OBJC_CLASS_$_GCGenericDeviceDataElementExistsExpressionModel
+ _OBJC_CLASS_$_GCGenericDeviceDataElementExistsExpressionModelBuilder
+ _OBJC_CLASS_$_GCGenericDeviceDriverPropertiesModel
+ _OBJC_CLASS_$_GCGenericDeviceDriverPropertiesModelBuilder
+ _OBJC_CLASS_$_GCGenericDeviceDriverPropertyModel
+ _OBJC_CLASS_$_GCGenericDeviceDriverPropertyModelBuilder
+ _OBJC_IVAR_$_GCGenericDeviceDataElementExistsExpressionModel._elementIdentifier
+ _OBJC_IVAR_$_GCGenericDeviceDataElementExistsExpressionModel._falseExpression
+ _OBJC_IVAR_$_GCGenericDeviceDataElementExistsExpressionModel._trueExpression
+ _OBJC_IVAR_$_GCGenericDeviceDataElementExistsExpressionModelBuilder._elementIdentifier
+ _OBJC_IVAR_$_GCGenericDeviceDataElementExistsExpressionModelBuilder._falseExpression
+ _OBJC_IVAR_$_GCGenericDeviceDataElementExistsExpressionModelBuilder._trueExpression
+ _OBJC_IVAR_$_GCGenericDeviceDriverModel._properties
+ _OBJC_IVAR_$_GCGenericDeviceDriverModelBuilder._properties
+ _OBJC_IVAR_$_GCGenericDeviceDriverPropertiesModel._properties
+ _OBJC_IVAR_$_GCGenericDeviceDriverPropertiesModelBuilder._properties
+ _OBJC_IVAR_$_GCGenericDeviceDriverPropertyModel._name
+ _OBJC_IVAR_$_GCGenericDeviceDriverPropertyModel._valueExpression
+ _OBJC_IVAR_$_GCGenericDeviceDriverPropertyModelBuilder._name
+ _OBJC_IVAR_$_GCGenericDeviceDriverPropertyModelBuilder._valueExpression
+ _OBJC_IVAR_$_GCGenericDeviceElementModel._optional
+ _OBJC_IVAR_$_GCGenericDeviceElementModelBuilder._optional
+ _OBJC_METACLASS_$_GCGenericDeviceDataElementExistsExpressionModel
+ _OBJC_METACLASS_$_GCGenericDeviceDataElementExistsExpressionModelBuilder
+ _OBJC_METACLASS_$_GCGenericDeviceDriverPropertiesModel
+ _OBJC_METACLASS_$_GCGenericDeviceDriverPropertiesModelBuilder
+ _OBJC_METACLASS_$_GCGenericDeviceDriverPropertyModel
+ _OBJC_METACLASS_$_GCGenericDeviceDriverPropertyModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataElementExistsExpressionModel
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataElementExistsExpressionModelBuilder(Serialization)
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDriverPropertiesModel(Serialization)
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDriverPropertiesModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDriverPropertyModel(Serialization)
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDriverPropertyModelBuilder
+ __OBJC_$_CLASS_PROP_LIST_GCGenericDeviceDriverPropertiesModel
+ __OBJC_$_CLASS_PROP_LIST_GCGenericDeviceDriverPropertiesModelBuilder
+ __OBJC_$_CLASS_PROP_LIST_GCGenericDeviceDriverPropertyModel
+ __OBJC_$_CLASS_PROP_LIST_GCGenericDeviceDriverPropertyModelBuilder
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataElementExistsExpressionModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataElementExistsExpressionModelBuilder(Serialization)
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertiesModel(Serialization)
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertiesModelBuilder
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertyModel(Serialization)
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertyModelBuilder
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceDataElementExistsExpressionModel
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceDataElementExistsExpressionModelBuilder
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceDriverPropertiesModel
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceDriverPropertiesModelBuilder
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceDriverPropertyModel
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceDriverPropertyModelBuilder
+ __OBJC_$_PROP_LIST_GCGenericDeviceDataElementExistsExpressionModel
+ __OBJC_$_PROP_LIST_GCGenericDeviceDataElementExistsExpressionModelBuilder
+ __OBJC_$_PROP_LIST_GCGenericDeviceDriverPropertiesModel
+ __OBJC_$_PROP_LIST_GCGenericDeviceDriverPropertiesModelBuilder
+ __OBJC_$_PROP_LIST_GCGenericDeviceDriverPropertyModel
+ __OBJC_$_PROP_LIST_GCGenericDeviceDriverPropertyModelBuilder
+ __OBJC_CLASS_PROTOCOLS_$_GCGenericDeviceDriverPropertiesModel
+ __OBJC_CLASS_PROTOCOLS_$_GCGenericDeviceDriverPropertyModel
+ __OBJC_CLASS_RO_$_GCGenericDeviceDataElementExistsExpressionModel
+ __OBJC_CLASS_RO_$_GCGenericDeviceDataElementExistsExpressionModelBuilder
+ __OBJC_CLASS_RO_$_GCGenericDeviceDriverPropertiesModel
+ __OBJC_CLASS_RO_$_GCGenericDeviceDriverPropertiesModelBuilder
+ __OBJC_CLASS_RO_$_GCGenericDeviceDriverPropertyModel
+ __OBJC_CLASS_RO_$_GCGenericDeviceDriverPropertyModelBuilder
+ __OBJC_METACLASS_RO_$_GCGenericDeviceDataElementExistsExpressionModel
+ __OBJC_METACLASS_RO_$_GCGenericDeviceDataElementExistsExpressionModelBuilder
+ __OBJC_METACLASS_RO_$_GCGenericDeviceDriverPropertiesModel
+ __OBJC_METACLASS_RO_$_GCGenericDeviceDriverPropertiesModelBuilder
+ __OBJC_METACLASS_RO_$_GCGenericDeviceDriverPropertyModel
+ __OBJC_METACLASS_RO_$_GCGenericDeviceDriverPropertyModelBuilder
+ ___95+[GCGenericDeviceDriverPropertiesModel(Serialization) modelWithDictionaryRepresentation:error:]_block_invoke
+ _objc_msgSend$optional
+ _objc_msgSend$properties
+ _objc_msgSend$setOptional:
+ _objc_msgSend$setProperties:
CStrings:
+ "'%@' <- %@"
+ "'properties' can not be nil"
+ "(element-exists '%@'\n\t%@\n\t%@\n)"
+ "<%@ %p> {\n\t elementIdentifier = %@\n\t trueExpression = %@\n\t falseExpression = %@\n}"
+ "<%@ %p> {\n\t elements = %@\n\t properties = %@\n\t input = %@\n\t rumble = %@\n}"
+ "<%@ %p> {\n\t identifier = %@\n\t predicate = %@\n\t optional = %d\n\t type (override) = %i\n}"
+ "<%@ %p> {\n\t name = %@\n\t valueExpression = %@\n}"
+ "<%@ %p> {\n\t properties = %@\n}"
+ "@\"GCGenericDeviceDriverPropertiesModel\""
+ "Did not find required element matching predicate for '%@'."
+ "Driver Properties"
+ "Driver Property"
+ "Element Exists Expression"
+ "GCGenericDeviceDataElementExistsExpressionModel"
+ "GCGenericDeviceDataElementExistsExpressionModel.m"
+ "GCGenericDeviceDataElementExistsExpressionModelBuilder"
+ "GCGenericDeviceDriverPropertiesModel"
+ "GCGenericDeviceDriverPropertiesModel.m"
+ "GCGenericDeviceDriverPropertiesModelBuilder"
+ "GCGenericDeviceDriverPropertyModel"
+ "GCGenericDeviceDriverPropertyModel.m"
+ "GCGenericDeviceDriverPropertyModelBuilder"
+ "Optional"
+ "Properties"
+ "T@\"GCGenericDeviceDriverPropertiesModel\",C,N,V_properties"
+ "T@\"GCGenericDeviceDriverPropertiesModel\",R,C,V_properties"
+ "T@\"NSSet\",C,N,V_properties"
+ "T@\"NSSet\",R,C,V_properties"
+ "TB,N,V_optional"
+ "TB,R,V_optional"
+ "_optional"
+ "_properties"
+ "optional"
+ "properties"
+ "setOptional:"
+ "setProperties:"
- "<%@ %p> {\n\t elements = %@\n\t input = %@\n\t rumble = %@\n}"
- "<%@ %p> {\n\t identifier = %@\n\t predicate = %@\n\t type (override) = %i\n}"
- "Did not find element matching predicate for '%@'."

```
