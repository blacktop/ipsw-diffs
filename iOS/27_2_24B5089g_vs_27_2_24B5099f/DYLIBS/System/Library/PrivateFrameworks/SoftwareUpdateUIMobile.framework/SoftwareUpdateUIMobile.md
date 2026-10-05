## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-772.40.11.0.0
-  __TEXT.__text: 0x7e95c
+772.40.12.0.0
+  __TEXT.__text: 0x7f4f0
   __TEXT.__objc_methlist: 0x287c
   __TEXT.__const: 0x450
-  __TEXT.__cstring: 0x52f7
-  __TEXT.__oslogstring: 0x8558
-  __TEXT.__gcc_except_tab: 0x149c
+  __TEXT.__cstring: 0x5327
+  __TEXT.__oslogstring: 0x85c8
+  __TEXT.__gcc_except_tab: 0x15a4
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x235
   __TEXT.__swift5_builtin: 0x14

   __DATA_CONST.__objc_selrefs: 0x1910
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__got: 0x920
   __AUTH_CONST.__const: 0x938
-  __AUTH_CONST.__cfstring: 0x2080
+  __AUTH_CONST.__cfstring: 0x20a0
   __AUTH_CONST.__objc_const: 0x7f88
   __AUTH_CONST.__auth_got: 0x6e0
   __AUTH.__objc_data: 0xc90

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1168
-  Symbols:   2035
-  CStrings:  772
+  Symbols:   2036
+  CStrings:  775
 
Symbols:
+ _kCFNull
Functions:
~ -[SUUIMobileAnalyticsReporter toSUAnalyticsEvent:] : 680 -> 1172
~ -[SUUIMobileAnalyticsReporter eventNameFor:] : 144 -> 176
~ _SUUIMobileDescriptorAgreementTypeToString : 172 -> 236
~ -[SUUIMobileDescriptorAgreementStatusRegistry agreementStatusForType:descriptor:] : 1324 -> 1372
~ -[SUUIMobileDescriptorAgreementStatusRegistry description] : 1892 -> 2572
~ -[SUUIMobileDescriptorAgreementStatusRegistry initWithCoder:] : 936 -> 2584
CStrings:
+ "%s: Could not assign the SUAnalyticsEvent user interaction type - %{public}@ does not map to a known interaction."
+ "-[SUUIMobileAnalyticsReporter toSUAnalyticsEvent:]"
+ "<unknown %@: %lld>"
+ "type"
- "suUserInteraction != nil"
```
