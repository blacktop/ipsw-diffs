## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/Versions/A/RunningBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1072.0.0.0.0
-  __TEXT.__text: 0x807ac
+1078.0.0.0.0
+  __TEXT.__text: 0x80874
   __TEXT.__objc_methlist: 0x63cc
   __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x6dde
-  __TEXT.__oslogstring: 0xb674
-  __TEXT.__gcc_except_tab: 0xb14
+  __TEXT.__cstring: 0x6d49
+  __TEXT.__oslogstring: 0xb6c3
+  __TEXT.__gcc_except_tab: 0xb24
   __TEXT.__unwind_info: 0x1b68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e38
+  __DATA_CONST.__objc_selrefs: 0x2e48
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x750
   __DATA_CONST.__got: 0x780
   __AUTH_CONST.__const: 0x1d30
-  __AUTH_CONST.__cfstring: 0x5d20
+  __AUTH_CONST.__cfstring: 0x5ce0
   __AUTH_CONST.__objc_const: 0xdb18
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x460

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 2906
-  Symbols:   6259
-  CStrings:  1736
+  Symbols:   6258
+  CStrings:  1735
 
Symbols:
+ _objc_msgSend$daemonJobLabel
+ _objc_msgSend$initWithAuditToken:
- _objc_msgSend$_preflightEligibility:
- _objc_msgSend$_preflightPrivacyDisclosure:
- _objc_msgSend$_preflightRestrictions:
Functions:
~ -[RBPowerAssertion description] : 164 -> 192
~ ___26-[RBProcess _lock_suspend]_block_invoke : 980 -> 1372
~ -[RBLaunchdProperties _parseAdditionalProperties:] : 1532 -> 1684
~ -[RBSLaunchContext(RBLaunchChecks) _passesPreflightChecksWithError:] : 496 -> 52
~ __errorWithRequestCode -> -[RBSLaunchContext(RBLaunchChecks) _launchAllowedBySystemState:error:] : 192 -> 992
~ -[RBSLaunchContext(RBLaunchChecks) _launchAllowedBySystemState:error:] -> __errorWithRequestCode : 992 -> 192
~ -[RBProcessManager _lifecycleQueue_addProcessWithInstance:properties:] : 2572 -> 2644
CStrings:
+ "%{public}@ host process %{public}@ is no longer alive; about to terminate"
+ "%{public}@ is already dead; using INVALID_AUDIT_TOKEN_VALUE"
+ "com.apple.FileProvider"
- "%{public}@ Cannot track instance that is already dead!"
- "Launch prevented due to device eligibility requirements"
- "Launch prevented due to partner financing restriction"
- "Launch prevented due to user approval regulatory requirements"
```
