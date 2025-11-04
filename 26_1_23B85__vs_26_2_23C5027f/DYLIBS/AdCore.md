## AdCore

> `/System/Library/PrivateFrameworks/AdCore.framework/AdCore`

```diff

-637.1.13.0.0
-  __TEXT.__text: 0x2cee8
+637.2.1.0.0
+  __TEXT.__text: 0x2e0d8
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x3e0c
+  __TEXT.__objc_methlist: 0x3fdc
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x3d93
+  __TEXT.__cstring: 0x3dd1
   __TEXT.__gcc_except_tab: 0x4a8
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xba8
-  __TEXT.__objc_classname: 0x3a2
-  __TEXT.__objc_methname: 0x711b
-  __TEXT.__objc_methtype: 0xab7
-  __TEXT.__objc_stubs: 0x3f20
-  __DATA_CONST.__got: 0x330
+  __TEXT.__unwind_info: 0xc00
+  __TEXT.__objc_classname: 0x3bf
+  __TEXT.__objc_methname: 0x7330
+  __TEXT.__objc_methtype: 0xacd
+  __TEXT.__objc_stubs: 0x4000
+  __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x6a8
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f10
+  __DATA_CONST.__objc_selrefs: 0x1f90
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__auth_got: 0x490
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x4b00
-  __AUTH_CONST.__objc_const: 0x5860
+  __AUTH_CONST.__cfstring: 0x4b80
+  __AUTH_CONST.__objc_const: 0x5b10
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x3c8
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x3d8
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__bss: 0x240

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9ED14F2-F5C9-3925-A430-AD4046399B07
-  Functions: 1364
-  Symbols:   4265
-  CStrings:  2799
+  UUID: 9463E3A5-3370-35B3-99DA-B3CB8262369E
+  Functions: 1402
+  Symbols:   4371
+  CStrings:  2834
 
Symbols:
+ +[ADTriggerContainer clientSideTriggersType]
+ -[ADSponsoredSearchRequest hasTriggersContainer]
+ -[ADSponsoredSearchRequest setTriggersContainer:]
+ -[ADSponsoredSearchRequest triggersContainer]
+ -[ADTrigger .cxx_destruct]
+ -[ADTrigger copyTo:]
+ -[ADTrigger copyWithZone:]
+ -[ADTrigger description]
+ -[ADTrigger dictionaryRepresentation]
+ -[ADTrigger experimentId]
+ -[ADTrigger hasExperimentId]
+ -[ADTrigger hasTreatmentId]
+ -[ADTrigger hash]
+ -[ADTrigger isEqual:]
+ -[ADTrigger mergeFrom:]
+ -[ADTrigger readFrom:]
+ -[ADTrigger setExperimentId:]
+ -[ADTrigger setTreatmentId:]
+ -[ADTrigger treatmentId]
+ -[ADTrigger writeTo:]
+ -[ADTriggerContainer .cxx_destruct]
+ -[ADTriggerContainer addClientSideTriggers:]
+ -[ADTriggerContainer clearClientSideTriggers]
+ -[ADTriggerContainer clientSideTriggersAtIndex:]
+ -[ADTriggerContainer clientSideTriggersCount]
+ -[ADTriggerContainer clientSideTriggers]
+ -[ADTriggerContainer copyTo:]
+ -[ADTriggerContainer copyWithZone:]
+ -[ADTriggerContainer description]
+ -[ADTriggerContainer dictionaryRepresentation]
+ -[ADTriggerContainer hash]
+ -[ADTriggerContainer isEqual:]
+ -[ADTriggerContainer mergeFrom:]
+ -[ADTriggerContainer readFrom:]
+ -[ADTriggerContainer setClientSideTriggers:]
+ -[ADTriggerContainer writeTo:]
+ OBJC_IVAR_$_ADSponsoredSearchRequest._triggersContainer
+ OBJC_IVAR_$_ADTrigger._experimentId
+ OBJC_IVAR_$_ADTrigger._treatmentId
+ OBJC_IVAR_$_ADTriggerContainer._clientSideTriggers
+ _ADTriggerContainerReadFrom
+ _ADTriggerReadFrom
+ _OBJC_CLASS_$_ADTrigger
+ _OBJC_CLASS_$_ADTriggerContainer
+ _OBJC_METACLASS_$_ADTrigger
+ _OBJC_METACLASS_$_ADTriggerContainer
+ __OBJC_$_CLASS_METHODS_ADTriggerContainer
+ __OBJC_$_INSTANCE_METHODS_ADTrigger
+ __OBJC_$_INSTANCE_METHODS_ADTriggerContainer
+ __OBJC_$_INSTANCE_VARIABLES_ADTrigger
+ __OBJC_$_INSTANCE_VARIABLES_ADTriggerContainer
+ __OBJC_$_PROP_LIST_ADTrigger
+ __OBJC_$_PROP_LIST_ADTriggerContainer
+ __OBJC_CLASS_PROTOCOLS_$_ADTrigger
+ __OBJC_CLASS_PROTOCOLS_$_ADTriggerContainer
+ __OBJC_CLASS_RO_$_ADTrigger
+ __OBJC_CLASS_RO_$_ADTriggerContainer
+ __OBJC_METACLASS_RO_$_ADTrigger
+ __OBJC_METACLASS_RO_$_ADTriggerContainer
+ _objc_msgSend$addClientSideTriggers:
+ _objc_msgSend$clearClientSideTriggers
+ _objc_msgSend$clientSideTriggersAtIndex:
+ _objc_msgSend$clientSideTriggersCount
+ _objc_msgSend$setExperimentId:
+ _objc_msgSend$setTreatmentId:
+ _objc_msgSend$setTriggersContainer:
CStrings:
+ "@\"ADTriggerContainer\""
+ "ADTrigger"
+ "ADTriggerContainer"
+ "T@\"ADTriggerContainer\",&,N,V_triggersContainer"
+ "T@\"NSMutableArray\",&,N,V_clientSideTriggers"
+ "T@\"NSString\",&,N,V_experimentId"
+ "T@\"NSString\",&,N,V_treatmentId"
+ "_clientSideTriggers"
+ "_experimentId"
+ "_treatmentId"
+ "_triggersContainer"
+ "addClientSideTriggers:"
+ "clearClientSideTriggers"
+ "clientSideTriggers"
+ "clientSideTriggersAtIndex:"
+ "clientSideTriggersCount"
+ "clientSideTriggersType"
+ "experimentId"
+ "hasExperimentId"
+ "hasTreatmentId"
+ "hasTriggersContainer"
+ "setClientSideTriggers:"
+ "setExperimentId:"
+ "setTreatmentId:"
+ "setTriggersContainer:"
+ "treatmentId"
+ "triggersContainer"

```
