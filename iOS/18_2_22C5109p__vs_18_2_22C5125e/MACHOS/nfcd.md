## nfcd

> `/usr/libexec/nfcd`

```diff

-352.7.0.0.0
-  __TEXT.__text: 0x269a00
+352.10.1.0.0
+  __TEXT.__text: 0x26acac
   __TEXT.__auth_stubs: 0x17c0
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_stubs: 0xd8a0
-  __TEXT.__objc_methlist: 0x785c
-  __TEXT.__const: 0x11c0
-  __TEXT.__oslogstring: 0x240c3
-  __TEXT.__cstring: 0x2de02
-  __TEXT.__objc_classname: 0x1bad
-  __TEXT.__objc_methname: 0x16b1f
-  __TEXT.__objc_methtype: 0x5331
-  __TEXT.__gcc_except_tab: 0x7674
+  __TEXT.__objc_stubs: 0xd8e0
+  __TEXT.__objc_methlist: 0x7874
+  __TEXT.__const: 0x11d0
+  __TEXT.__oslogstring: 0x24208
+  __TEXT.__cstring: 0x2df77
+  __TEXT.__objc_classname: 0x1bb0
+  __TEXT.__objc_methname: 0x16b97
+  __TEXT.__objc_methtype: 0x5373
+  __TEXT.__gcc_except_tab: 0x79d8
   __TEXT.__dlopen_cstrs: 0x5a1
-  __TEXT.__unwind_info: 0x36a8
+  __TEXT.__unwind_info: 0x3730
   __DATA_CONST.__auth_got: 0xbf0
   __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x7948
-  __DATA_CONST.__cfstring: 0x101c0
+  __DATA_CONST.__const: 0x7998
+  __DATA_CONST.__cfstring: 0x10220
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x380

   __DATA_CONST.__objc_arraydata: 0x1df0
   __DATA_CONST.__objc_arrayobj: 0x378
   __DATA_CONST.__objc_dictobj: 0xf28
-  __DATA.__objc_const: 0x16c38
-  __DATA.__objc_selrefs: 0x5268
-  __DATA.__objc_ivar: 0xf54
+  __DATA.__objc_const: 0x16c58
+  __DATA.__objc_selrefs: 0x5280
+  __DATA.__objc_ivar: 0xf58
   __DATA.__objc_data: 0x3930
   __DATA.__data: 0x2ab0
   __DATA.__bss: 0x518

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4360
+  Functions: 4367
   Symbols:   525
-  CStrings:  12076
+  CStrings:  12095
 
CStrings:
+ "\x11\x13"
+ "%!@(MISSING) for %!@(MISSING) (%!d(MISSING)) for %!f(MISSING) seconds"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) %!{(MISSING)public}@ for %!{(MISSING)public}@ (%!d(MISSING)) for %!f(MISSING) seconds"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Done running script. Status = %!l(MISSING)d, error = %!@(MISSING)"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Ignoring Express type None"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Previously invalidated"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Processing %!{(MISSING)public}@ : Known HW state = %!u(MISSING)"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Session in suspended queue:"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Type-F express entered for unknown system code 0x%!x(MISSING)?"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) VAS express entered but field is non-ECP?"
+ "%!{(MISSING)public, signpost.description:begin_time}llu"
+ "-[NFWalletPresentationService presentWithUserInfo:completion:]"
+ "@48@0:8@16@24@32Q40"
+ "@64@0:8@16@24@32^q40^Q48^B56"
+ "NFCD built from (B&I) Stockholm_Base-352.10.1"
+ "SignpostBeginTime"
+ "SuspendedSessionQueue"
+ "WalletPresentTotalDuration"
+ "_createResponseFromCommand:params:rapdu:duration:"
+ "_executeCommands:params:completion:"
+ "_invalidated"
+ "_keybagUpdate"
+ "_sendOneCommand:params:responses:lastStatus:totalTXTime:failureDetected:"
+ "presentWithUserInfo:completion:"
+ "startISO18013WithConnectionHandoverConfiguration:type:credentialType:delegate:"
+ "v32@0:8@\"NSDictionary\"16@?<v@?>24"
+ "v44@?0@\"NSError\"8q16Q24B32@\"NSArray\"36"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Previously started"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Previously stopped"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) contactless TC already set"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) contactless transaction codes can't be nil"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) express mode set to none - ignoring"
- "-[NFWalletPresentationService presentWithCompletion:]"
- "NFCD built from (B&I) Stockholm_Base-352.7"
- "_executeCommands:params:responses:lastSWStatus:totalAPDUTxTimeInMS:appletResponseFailure:"
- "presentWithCompletion:"
- "startISO18013WithConnectionHandoverConfiguration:type:delegate:"
- "v24@0:8@?<v@?>16"

```
