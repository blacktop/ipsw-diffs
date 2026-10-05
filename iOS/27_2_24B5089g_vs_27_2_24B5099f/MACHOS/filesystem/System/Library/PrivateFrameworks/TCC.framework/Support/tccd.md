## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`

```diff

-919.0.0.0.0
-  __TEXT.__text: 0x8e498
+921.0.0.0.0
+  __TEXT.__text: 0x8fa64
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0xbb60
-  __TEXT.__objc_methlist: 0x5754
-  __TEXT.__cstring: 0x1366f
+  __TEXT.__objc_stubs: 0xbd00
+  __TEXT.__objc_methlist: 0x57d4
+  __TEXT.__cstring: 0x13838
   __TEXT.__const: 0x6f8
-  __TEXT.__gcc_except_tab: 0x31fc
-  __TEXT.__objc_methname: 0x138f5
-  __TEXT.__oslogstring: 0x11095
+  __TEXT.__gcc_except_tab: 0x32f4
+  __TEXT.__objc_methname: 0x13c02
+  __TEXT.__oslogstring: 0x1135e
   __TEXT.__objc_classname: 0x6f2
   __TEXT.__objc_methtype: 0x2383
   __TEXT.__dlopen_cstrs: 0xd9
-  __TEXT.__unwind_info: 0x2580
-  __DATA_CONST.__const: 0x2920
-  __DATA_CONST.__cfstring: 0x8e40
+  __TEXT.__unwind_info: 0x25e8
+  __DATA_CONST.__const: 0x29b0
+  __DATA_CONST.__cfstring: 0x8f00
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0xf28
   __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__got: 0x4e8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0xa758
-  __DATA.__objc_selrefs: 0x3840
-  __DATA.__objc_ivar: 0x770
+  __DATA.__objc_const: 0xa848
+  __DATA.__objc_selrefs: 0x38b0
+  __DATA.__objc_ivar: 0x784
   __DATA.__objc_data: 0x13b0
-  __DATA.__data: 0x738
+  __DATA.__data: 0x740
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3104
+  Functions: 3136
   Symbols:   512
-  CStrings:  6055
+  CStrings:  6102
 
CStrings:
+ "%s: %{public}@ does not support reminder prompts, ignoring report-use"
+ "%s: HealthKit framework not available, no source name for %{public}@"
+ "%s: HealthKit knows no source name for %{public}@"
+ "%s: automaticTimeOverride=ForceDisabled, not surfacing reminder prompt"
+ "%s: could not create the authorization store for %{public}@"
+ "%s: missing client or service, refusing to enqueue"
+ "%s: no authorization records for %{public}@: %{public}@"
+ "%s: resolved %{public}@ to %{public}@"
+ "%s: source %{public}@ is not an installed bundle"
+ "%s: source fetch failed for %{public}@: %{public}@"
+ "%s: timed out fetching authorization records for %{public}@"
+ "%s: timed out resolving the source name for %{public}@"
+ "-[TCCDReminderMonitor healthSourceNameForBundleIdentifier:]"
+ "-[TCCDReminderMonitor healthSourceNameForBundleIdentifier:]_block_invoke"
+ "A2"
+ "AUTHREQ_CTX: msgID=%{public}@, function=%@, service=%@, query=%llu, client_dict=%@, daemon_dict=%@, attributed_bundle_id=%{public}@"
+ "Invalid attributed bundle identifier: %@"
+ "T@\"NSString\",C,N,V_attributedBundleIdentifier"
+ "T@\"NSString\",C,N,V_attributedDisplayName"
+ "T@\"NSString\",C,N,V_reminderDisplayBundleIdentifier"
+ "TB,N,V_supportsAttributedReportUse"
+ "TCCD_MSG_MESSAGE_OPTION_ATTRIBUTED_BUNDLE_IDENTIFIER_KEY"
+ "Tq,V_automaticTimeOverride"
+ "_attributedBundleIdentifier"
+ "_attributedDisplayName"
+ "_automaticTimeOverride"
+ "_reminderDisplayBundleIdentifier"
+ "_supportsAttributedReportUse"
+ "attributedBundleIdentifier"
+ "attributedDisplayName"
+ "automaticTimeOverride"
+ "characterAtIndex:"
+ "com.apple.os-eligibility-domain.change.carabus"
+ "display_client"
+ "fetchAuthorizationRecordsForBundleIdentifier:error:"
+ "fetchSourcesRequestingAuthorizationForTypes:completion:"
+ "healthSourceNameForBundleIdentifier:"
+ "identifier exceeds maximum length of %lu"
+ "identifier must be printable ASCII"
+ "identifier must be valid UTF-8"
+ "identifier must not be empty"
+ "reminderDisplayBundleIdentifier"
+ "setAttributedBundleIdentifier:"
+ "setAttributedDisplayName:"
+ "setAutomaticTimeOverride:"
+ "setReminderDisplayBundleIdentifier:"
+ "setSupportsAttributedReportUse:"
+ "supportsAttributedReportUse"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
+ "\xf0\xf0\xf0\xf01\xf0c"
- "A\""
- "AUTHREQ_CTX: msgID=%{public}@, function=%@, service=%@, query=%llu, client_dict=%@, daemon_dict=%@"
- "\xf0\xf0\xf0\xf0!\xf0c"
```
