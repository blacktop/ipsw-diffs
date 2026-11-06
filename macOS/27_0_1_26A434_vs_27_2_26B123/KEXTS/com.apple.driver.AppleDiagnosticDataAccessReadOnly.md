## com.apple.driver.AppleDiagnosticDataAccessReadOnly

> `com.apple.driver.AppleDiagnosticDataAccessReadOnly`

```diff

-55.0.0.0.0
+55.40.3.0.0
   __TEXT.__cstring: 0x270
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x10fc
+  __TEXT_EXEC.__text: 0x1144
   __TEXT_EXEC.__auth_stubs: 0x160
   __DATA.__data: 0xc8
   __DATA.__common: 0x38
Symbols:
+ __ZN33AppleDiagnosticDataAccessReadOnly11_readRegionEP22AppleARMNORFlashDeviceP21AppleNANDConfigAccessjPhyy
- __ZN33AppleDiagnosticDataAccessReadOnly11_readRegionEjjPhyy
Functions:
~ __ZN33AppleDiagnosticDataAccessReadOnly5startEP9IOService : 956 -> 1044
~ __ZNK33AppleDiagnosticDataAccessReadOnly11getPropertyEPK8OSSymbol -> __ZN33AppleDiagnosticDataAccessReadOnly13_lazyLoadDataEjb : 248 -> 884
~ __ZNK33AppleDiagnosticDataAccessReadOnly18_regionIndexForKeyEPK8OSString -> __ZNK33AppleDiagnosticDataAccessReadOnly11getPropertyEPK8OSSymbol : 124 -> 248
~ __ZN33AppleDiagnosticDataAccessReadOnly13_lazyLoadDataEjb -> __ZNK33AppleDiagnosticDataAccessReadOnly18_regionIndexForKeyEPK8OSString : 816 -> 124
~ __ZN33AppleDiagnosticDataAccessReadOnly11_readRegionEjjPhyy -> __ZN33AppleDiagnosticDataAccessReadOnly11_readRegionEP22AppleARMNORFlashDeviceP21AppleNANDConfigAccessjPhyy : 244 -> 160
```
