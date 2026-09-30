## STAEAExtractionPlugin

> `/System/Library/StreamingExtractorPlugins/STAEAExtractionPlugin.bundle/STAEAExtractionPlugin`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0x41c0
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x2d4
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0xaa3
-  __TEXT.__oslogstring: 0x534
-  __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__objc_methname: 0x746
-  __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methtype: 0x29b
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x1c8
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x460
-  __DATA_CONST.__objc_classlist: 0x8
+43.0.0.0.1
+  __TEXT.__text: 0x4cd8
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x35c
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xc86
+  __TEXT.__objc_methname: 0x846
+  __TEXT.__oslogstring: 0x716
+  __TEXT.__objc_classname: 0x4a
+  __TEXT.__objc_methtype: 0x2ca
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x4f0
-  __DATA.__objc_selrefs: 0x228
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__objc_data: 0x50
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x610
+  __DATA.__objc_selrefs: 0x260
+  __DATA.__objc_ivar: 0x48
+  __DATA.__objc_data: 0xa0
   __DATA.__data: 0xd8
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD172CA2-8039-3EAE-9848-5439741DE66C
-  Functions: 99
-  Symbols:   92
-  CStrings:  271
+  UUID: 8B7AD3CE-95B2-33DD-BC0B-50D144DEC4B3
+  Functions: 118
+  Symbols:   101
+  CStrings:  315
 
Symbols:
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_STReservableSpacePolicy
+ _OBJC_METACLASS_$_STReservableSpacePolicy
+ _STReservableSpacePolicyErrorDomain
+ _getiopolicy_np
+ _objc_alloc
+ _objc_autorelease
+ _objc_retain_x19
+ _objc_retain_x8
+ _setiopolicy_np
- _STGetLoggingCategory
CStrings:
+ "%{public}s: Invalidating the reservable space policy failed: %@"
+ "-[STReservableSpacePolicy invalidate]"
+ "<nil>"
+ "@24@0:8^@16"
+ "@32@0:8Q16^@24"
+ "A per-process policy for reservable space access is already enabled."
+ "A per-thread policy for reservable space access is already enabled."
+ "AB"
+ "B"
+ "Failed to set the reserve access policy for the current process."
+ "Failed to set the reserve access policy for the current thread."
+ "Getting the reserve access policy for the current process failed."
+ "Getting the reserve access policy for the current thread failed."
+ "NO"
+ "STReservableSpacePolicy"
+ "STReservableSpacePolicyErrorDomain"
+ "TB,R,N,V_usesReserveAccessPolicy"
+ "TQ,N,V_policyType"
+ "YES"
+ "[%@] %{public}s: Failed to create a reservable space policy while bytes are being received: %@"
+ "[%@] %{public}s: Failed to create a reservable space policy while finishing the stream: %@"
+ "[%@] %{public}s: Failed to create a reservable space policy while preparing for extraction: %@"
+ "[%@] %{public}s: Failed to create a reservable space policy while suspending the stream: %@"
+ "[%@] %{public}s: new AEA extractor (SessionID: %@, UsesReserveAccessPolicy: %@)"
+ "__setErrorForPtr:code:"
+ "_invalidated"
+ "_policyType"
+ "_usesReserveAccessPolicy"
+ "initWithPolicyType:errorPtr:"
+ "policyType"
+ "processPolicyWithErrorPtr:"
+ "setPolicyType:"
+ "threadPolicyWithErrorPtr:"
+ "usesReserveAccessPolicy"
+ "v32@0:8^@16Q24"
- "[%@] %{public}s: new AEA extractor"

```
