## AppleGameControllerPersonality_development

> `/System/Library/Extensions/AppleGameControllerPersonality.kext/AppleGameControllerPersonality_development`

```diff

-13.5.1.0.0
-  __TEXT.__cstring: 0xeb
-  __TEXT.__os_log: 0x53
-  __TEXT_EXEC.__text: 0x6e8
-  __TEXT_EXEC.__auth_stubs: 0xb0
+14.0.14.0.0
+  __TEXT.__cstring: 0x237
+  __TEXT.__os_log: 0x9f
+  __TEXT_EXEC.__text: 0x1bc4
+  __TEXT_EXEC.__auth_stubs: 0x140
   __DATA.__data: 0xc8
-  __DATA.__common: 0x38
-  __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x58
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__mod_init_func: 0x8
-  __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x788
-  __DATA_CONST.__kalloc_type: 0x40
-  UUID: DC4526C0-C283-323D-A711-ADB8B9EDE393
-  Functions: 24
-  Symbols:   279
-  CStrings:  13
+  __DATA.__common: 0x88
+  __DATA.__bss: 0x10
+  __DATA_CONST.__mod_init_func: 0x18
+  __DATA_CONST.__mod_term_func: 0x18
+  __DATA_CONST.__const: 0x1510
+  __DATA_CONST.__kalloc_type: 0xc0
+  __DATA_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x70
+  UUID: C32270AE-081F-3722-B129-EE538CFDA28E
+  Functions: 58
+  Symbols:   368
+  CStrings:  31
 
Symbols:
+ _GLOBAL__sub_I_AppleGCHIDProviderPropertyMerger.cpp
+ _GLOBAL__sub_I_AppleGCHIDUserEventDriver.cpp
+ __ZL29AppleGCHIDUserEventDriver_ktv
+ __ZL36AppleGCHIDProviderPropertyMerger_ktv
+ __ZN11OSMetaClass20getMetaClassWithNameEPK8OSSymbol
+ __ZN12OSDictionary14withDictionaryEPKS_j
+ __ZN12OSDictionary9metaClassE
+ __ZN15IORegistryEntry13setPropertiesEP8OSObject
+ __ZN20OSCollectionIterator14withCollectionEPK12OSCollection
+ __ZN24IOProviderPropertyMerger10gMetaClassE
+ __ZN24IOProviderPropertyMerger11setPropertyEPK8OSSymbolP8OSObject
+ __ZN24IOProviderPropertyMerger16setPropertyTableEP12OSDictionary
+ __ZN24IOProviderPropertyMerger4initEP12OSDictionary
+ __ZN24IOProviderPropertyMergerC2EPK11OSMetaClass
+ __ZN24IOProviderPropertyMergerD2Ev
+ __ZN25AppleGCHIDUserEventDriver10gMetaClassE
+ __ZN25AppleGCHIDUserEventDriver10superClassE
+ __ZN25AppleGCHIDUserEventDriver11handleStartEP9IOService
+ __ZN25AppleGCHIDUserEventDriver11setPropertyEPK8OSSymbolP8OSObject
+ __ZN25AppleGCHIDUserEventDriver12didTerminateEP9IOServicejPb
+ __ZN25AppleGCHIDUserEventDriver5probeEP9IOServicePi
+ __ZN25AppleGCHIDUserEventDriver9MetaClassC1Ev
+ __ZN25AppleGCHIDUserEventDriver9MetaClassC2Ev
+ __ZN25AppleGCHIDUserEventDriver9MetaClassD0Ev
+ __ZN25AppleGCHIDUserEventDriver9MetaClassD1Ev
+ __ZN25AppleGCHIDUserEventDriver9metaClassE
+ __ZN25AppleGCHIDUserEventDriverC1EPK11OSMetaClass
+ __ZN25AppleGCHIDUserEventDriverC1Ev
+ __ZN25AppleGCHIDUserEventDriverC2EPK11OSMetaClass
+ __ZN25AppleGCHIDUserEventDriverC2Ev
+ __ZN25AppleGCHIDUserEventDriverD0Ev
+ __ZN25AppleGCHIDUserEventDriverD1Ev
+ __ZN25AppleGCHIDUserEventDriverD2Ev
+ __ZN25AppleGCHIDUserEventDriverdlEPvm
+ __ZN25AppleGCHIDUserEventDrivernwEm
+ __ZN32AppleGCHIDProviderPropertyMerger10gMetaClassE
+ __ZN32AppleGCHIDProviderPropertyMerger10superClassE
+ __ZN32AppleGCHIDProviderPropertyMerger15mergePropertiesEP9IOServiceP12OSDictionary
+ __ZN32AppleGCHIDProviderPropertyMerger17mergeDictionariesEP12OSDictionaryS1_b
+ __ZN32AppleGCHIDProviderPropertyMerger5probeEP9IOServicePi
+ __ZN32AppleGCHIDProviderPropertyMerger9MetaClassC1Ev
+ __ZN32AppleGCHIDProviderPropertyMerger9MetaClassC2Ev
+ __ZN32AppleGCHIDProviderPropertyMerger9MetaClassD0Ev
+ __ZN32AppleGCHIDProviderPropertyMerger9MetaClassD1Ev
+ __ZN32AppleGCHIDProviderPropertyMerger9metaClassE
+ __ZN32AppleGCHIDProviderPropertyMergerC1EPK11OSMetaClass
+ __ZN32AppleGCHIDProviderPropertyMergerC1Ev
+ __ZN32AppleGCHIDProviderPropertyMergerC2EPK11OSMetaClass
+ __ZN32AppleGCHIDProviderPropertyMergerC2Ev
+ __ZN32AppleGCHIDProviderPropertyMergerD0Ev
+ __ZN32AppleGCHIDProviderPropertyMergerD1Ev
+ __ZN32AppleGCHIDProviderPropertyMergerD2Ev
+ __ZN32AppleGCHIDProviderPropertyMergerdlEPvm
+ __ZN32AppleGCHIDProviderPropertyMergernwEm
+ __ZN8OSNumber9metaClassE
+ __ZN8OSString9metaClassE
+ __ZN8OSSymbol10withStringEPK8OSString
+ __ZN8OSSymbol9metaClassE
+ __ZN9IOService10gMetaClassE
+ __ZN9IOService10handleOpenEPS_jPv
+ __ZN9IOService11handleCloseEPS_j
+ __ZN9IOService12didTerminateEPS_jPb
+ __ZN9IOService13newUserClientEP4taskPvjP12OSDictionaryPP12IOUserClient
+ __ZN9IOService18matchPropertyTableEP12OSDictionaryPi
+ __ZN9IOService4freeEv
+ __ZN9IOService4stopEPS_
+ __ZN9IOService5closeEPS_j
+ __ZN9IOService5startEPS_
+ __ZN9IOService7messageEjPS_Pv
+ __ZN9IOService8DispatchE5IORPC
+ __ZNK11OSMetaClass13getSuperClassEv
+ __ZNK25AppleGCHIDUserEventDriver12getMetaClassEv
+ __ZNK25AppleGCHIDUserEventDriver9MetaClass5allocEv
+ __ZNK32AppleGCHIDProviderPropertyMerger12getMetaClassEv
+ __ZNK32AppleGCHIDProviderPropertyMerger9MetaClass5allocEv
+ __ZNK9IOService12handleIsOpenEPKS_
+ __ZTV25AppleGCHIDUserEventDriver
+ __ZTV32AppleGCHIDProviderPropertyMerger
+ __ZTVN25AppleGCHIDUserEventDriver9MetaClassE
+ __ZTVN32AppleGCHIDProviderPropertyMerger9MetaClassE
+ __ZZN25AppleGCHIDUserEventDriver5probeEP9IOServicePiE11_os_log_fmt
+ __ZZN25AppleGCHIDUserEventDriver5probeEP9IOServicePiE11_os_log_fmt_0
+ _gIOProviderClassKey
+ _kOSBooleanFalse
+ _strlen
+ _strncmp
CStrings:
+ "12111112122212121"
+ "AppleGCHIDProviderPropertyMerger"
+ "AppleGCHIDUserEventDriver"
+ "AppleGCHIDUserEventDriver::probe()"
+ "CFBundleIdentifier"
+ "GCSyntheticDevice"
+ "HIDVirtualDevice"
+ "IOHID"
+ "IOProviderMergeProperties"
+ "IOProviderMergePropertiesTargetClass"
+ "IOUserClass"
+ "Not matching on HID device created by %s"
+ "PrimaryUsagePage"
+ "Privileged"
+ "_Privileged"
+ "com.apple."
+ "site.AppleGCHIDProviderPropertyMerger"
+ "site.AppleGCHIDUserEventDriver"

```
