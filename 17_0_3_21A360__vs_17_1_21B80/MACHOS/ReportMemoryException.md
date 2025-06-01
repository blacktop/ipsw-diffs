## ReportMemoryException

> `/usr/libexec/ReportMemoryException`

```diff

-240.0.0.0.0
-  __TEXT.__text: 0x82c0
+240.40.2.0.0
+  __TEXT.__text: 0x84fc
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0xe20
+  __TEXT.__objc_stubs: 0xea0
   __TEXT.__objc_methlist: 0x34
-  __TEXT.__cstring: 0xa12
+  __TEXT.__cstring: 0xa11
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__objc_methname: 0xa2f
-  __TEXT.__oslogstring: 0x1558
+  __TEXT.__objc_methname: 0xa8f
+  __TEXT.__oslogstring: 0x1692
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methtype: 0x49
   __TEXT.__unwind_info: 0x14c

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x148
-  __DATA.__objc_selrefs: 0x398
+  __DATA.__objc_selrefs: 0x3b8
   __DATA.__objc_classrefs: 0x90
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77CCE453-8FCE-306E-B259-53E5478B35D6
+  UUID: D222A4D7-AF71-396A-9BB1-23F97D8D0ABB
   Functions: 56
   Symbols:   156
-  CStrings:  355
+  CStrings:  363
 
CStrings:
+ "Attempting to save lite diagnostic before generating a memgraph for process %@ [%d]"
+ "Deleting initial lite diagnostic so we don't have 2 diagnostics on-device: %{public}@"
+ "Failed to delete %{public}@ due to error %@"
+ "Failed to save initial lite diagnostic for process %@: %{public}@"
+ "Successfully deleted %{public}@"
+ "Successfully saved initial lite diagnostic for process %@ at %@"
+ "_generateMemgraphWithContentLevel:timeoutSecs:memgraphFailedReasonOut:"
+ "_populateAddtionalMetadataWithOptions:timeoutSecs:"
+ "liteDiagFilePath"
+ "localizedDescription"
+ "memgraph %@ limit of %ld has already been exceeded in the last 24 hours"
+ "setLiteDiagFilePath:"
- "Failed to delete: %{public}@"
- "Successfully deleted: %{public}@"
- "_populateVerboseDiagnosticsWithOptions:contentLevel:timeoutSecs:memgraphFailedReasonOut:"
- "memgraph %@ limit of %ld has already been exceeded in the last 24 hours."

```
