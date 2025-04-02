## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

-835.0.0.0.0
-  __TEXT.__text: 0x80fa8
+840.0.0.0.0
+  __TEXT.__text: 0x81708
   __TEXT.__auth_stubs: 0x14c0
   __TEXT.__objc_stubs: 0xa420
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x5a24
+  __TEXT.__objc_methlist: 0x58ac
   __TEXT.__cstring: 0x3d2e
   __TEXT.__objc_classname: 0xb85
-  __TEXT.__objc_methname: 0xd272
-  __TEXT.__objc_methtype: 0x2cf8
+  __TEXT.__objc_methname: 0xd29a
+  __TEXT.__objc_methtype: 0x2cbf
   __TEXT.__const: 0x570
-  __TEXT.__gcc_except_tab: 0x9090
-  __TEXT.__oslogstring: 0xcffa
-  __TEXT.__unwind_info: 0x2958
+  __TEXT.__gcc_except_tab: 0x90f4
+  __TEXT.__oslogstring: 0xd4c9
+  __TEXT.__unwind_info: 0x2960
   __DATA_CONST.__auth_got: 0xa78
   __DATA_CONST.__got: 0x708
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x23f0
+  __DATA_CONST.__const: 0x2440
   __DATA_CONST.__cfstring: 0x4880
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x58

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xd678
-  __DATA.__objc_selrefs: 0x3548
+  __DATA.__objc_const: 0xd620
+  __DATA.__objc_selrefs: 0x3540
   __DATA.__objc_ivar: 0x544
   __DATA.__objc_data: 0x1590
   __DATA.__data: 0xf90

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2411
+  Functions: 2403
   Symbols:   593
-  CStrings:  4282
+  CStrings:  4294
 
CStrings:
+ "#E %s Retrieving passcode change information failed for account UUID %@, could not find context"
+ "#I %s Greeting change is %@ for account UUID %@"
+ "#I %s Maximum greeting duration is %d for account UUID %@"
+ "#I %s Maximum passcode length is %ld for account UUID %@"
+ "#I %s Minimum passcode length is %ld for account UUID %@"
+ "#I %s Passcode change is %@ for account UUID %@"
+ "#I %s Service state is '%@' for account UUID %@"
+ "#I %s Setting passcode %@ for service %@, accountUUID %@"
+ "#I %s%sCall voicemail is not supported for account UUID %@, invalid voicemail phoneNumber"
+ "#I %s%sCall voicemail is not supported for account UUID %@, voicemail service in not supported in carrier bundle"
+ "#W %s%sCall voicemail is not supported for account UUID %@, could not find context"
+ "#W %s%sRetrieving greeting change information failed for account UUID %@, could not find context"
+ "#W %s%sRetrieving greeting change information failed for account UUID %@, could not find service"
+ "#W %s%sRetrieving greeting failed for account UUID %@, could not find service"
+ "#W %s%sRetrieving maximum greeting duration failed for account UUID %@, could not find service"
+ "#W %s%sRetrieving maximum greeting duration failed for account account UUID %@, could not find context"
+ "#W %s%sRetrieving maximum passcode length failed for account UUID %@, could not find service"
+ "#W %s%sRetrieving minimum passcode length failed for account UUID %@, could not find service"
+ "#W %s%sRetrieving passcode change information failed for account UUID %@, could not find service"
+ "#W %s%sSet greeting failed for account UUID %@, could not find service"
+ "#W %s%sSet passcode failed for account UUID %@, could not find service"
+ "%@ %p for client [%s:%d] (conn=%p) Created"
+ "%@ %p for client [%s:%d] (conn=%p) Deleted"
+ "isAccountOnline:completion:"
+ "isAccountSubscribed:completion:"
+ "isCallVoicemailSupportedForAccountUUID:completion:"
+ "isGreetingChangeSupportedForAccountUUID:completion:"
+ "isPasscodeChangeSupportedForAccountUUID:completion:"
+ "maximumGreetingDurationForAccountUUID:completion:"
+ "maximumPasscodeLengthForAccountUUID:completion:"
+ "minimumPasscodeLengthForAccountUUID:completion:"
- "#I %s%sInvalid voicemail phoneNumber, call voicemail is not supported for account UUID %@"
- "#I %s%sSetting passcode for service %@: accountUUID: %@"
- "#I %s%sVoicemail service in not supported in carrier bundle, call voicemail is not supported for account UUID %@"
- "#W %s%sCould not retrieve context, call voicemail is not supported for account UUID %@"
- "#W %s%sCould not retrieve greeting controller for account UUID %@"
- "#W %s%sCould not retrieve service provider for account UUID %@"
- "B24@0:8@\"NSUUID\"16"
- "Greeting is %@ for account %@"
- "d24@0:8@\"NSUUID\"16"
- "isAccountOnline:"
- "isAccountSubscribed:"
- "isCallVoicemailSupportedForAccountUUID:"
- "isGreetingChangeSupportedForAccountUUID:"
- "isPasscodeChangeSupportedForAccountUUID:"
- "isPasswordChangeSupportedForDefaultSubscription"
- "maximumGreetingDurationForAccountUUID:"
- "maximumPasscodeLengthForAccountUUID:"
- "minimumPasscodeLengthForAccountUUID:"
- "q24@0:8@\"NSUUID\"16"

```
