## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3812.100.13.2.1
-  __TEXT.__text: 0x52e92c
-  __TEXT.__auth_stubs: 0x42d0
+3814.100.5.2.3
+  __TEXT.__text: 0x5420f4
+  __TEXT.__auth_stubs: 0x4380
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x140
-  __TEXT.__cstring: 0x894a
+  __TEXT.__objc_methlist: 0x198
+  __TEXT.__cstring: 0x8cfa
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x41b00
-  __TEXT.__swift5_typeref: 0xd037
-  __TEXT.__swift5_capture: 0x68f0
-  __TEXT.__constg_swiftt: 0xad10
-  __TEXT.__swift5_reflstr: 0xcc4d
-  __TEXT.__swift5_fieldmd: 0x113f0
-  __TEXT.__swift5_proto: 0x2290
-  __TEXT.__swift5_types: 0x1354
+  __TEXT.__const: 0x42390
+  __TEXT.__swift5_typeref: 0xd393
+  __TEXT.__swift5_capture: 0x6ab8
+  __TEXT.__constg_swiftt: 0xb260
+  __TEXT.__swift5_reflstr: 0xd00d
+  __TEXT.__swift5_fieldmd: 0x118fc
+  __TEXT.__swift5_proto: 0x230c
+  __TEXT.__swift5_types: 0x13b8
   __TEXT.__swift5_assocty: 0x18d0
-  __TEXT.__oslogstring: 0xd0a0
-  __TEXT.__swift5_builtin: 0xc44
-  __TEXT.__swift5_mpenum: 0xc20
-  __TEXT.__swift5_protos: 0x64
-  __TEXT.__objc_classname: 0x99
-  __TEXT.__objc_methname: 0x1581
+  __TEXT.__oslogstring: 0xda50
+  __TEXT.__swift5_builtin: 0xcbc
+  __TEXT.__swift5_mpenum: 0xc5c
+  __TEXT.__swift5_protos: 0x6c
+  __TEXT.__objc_classname: 0xbf
+  __TEXT.__objc_methname: 0x171f
   __TEXT.__objc_methtype: 0x3e5
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__unwind_info: 0x129c0
-  __TEXT.__eh_frame: 0x19190
-  __DATA_CONST.__auth_got: 0x2178
-  __DATA_CONST.__got: 0xad0
-  __DATA_CONST.__auth_ptr: 0x2c98
-  __DATA_CONST.__const: 0x465c0
+  __TEXT.__unwind_info: 0x12d08
+  __TEXT.__eh_frame: 0x193b8
+  __DATA_CONST.__auth_got: 0x21d0
+  __DATA_CONST.__got: 0xb00
+  __DATA_CONST.__auth_ptr: 0x2d70
+  __DATA_CONST.__const: 0x47288
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0x4798
-  __DATA.__objc_selrefs: 0x6f8
-  __DATA.__objc_data: 0x930
-  __DATA.__data: 0xe0e8
-  __DATA.__bss: 0x43eb0
-  __DATA.__common: 0xc98
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA.__objc_const: 0x4bb0
+  __DATA.__objc_selrefs: 0x788
+  __DATA.__objc_data: 0x980
+  __DATA.__data: 0xe6e8
+  __DATA.__bss: 0x44d30
+  __DATA.__common: 0xcc0
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 28221
-  Symbols:   426
-  CStrings:  2849
+  Functions: 28535
+  Symbols:   436
+  CStrings:  2936
 
Symbols:
+ _NSURLVolumeAvailableCapacityKey
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSExpression
+ _OBJC_CLASS_$_NSExpressionDescription
+ _SecTrustEvaluateAsyncWithError
+ _class_getClassMethod
+ _class_getInstanceMethod
+ _method_getImplementation
+ _sec_protocol_metadata_get_server_name
+ _sec_trust_copy_ref
- _NSURLVolumeAvailableCapacityForImportantUsageKey
CStrings:
+ "\x01\x02\x03\x04\x05\x06\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x1c\x1d\x1f\x18\x19\x1a\x1b\x1e !\"#$%!&(MISSING)'()"
+ "Available disk space changed. Free space: %!{(MISSING)iec-bytes}ld, for opportunistic use: %!{(MISSING)iec-bytes}ld"
+ "Checking current batch: not currently running request."
+ "Current ID {%!l(MISSING)d} higher than {%!l(MISSING)d}: Ignoring request to stop download."
+ "Current ID {%!l(MISSING)d} or higher than new {%!l(MISSING)d}: Ignoring request to start download. Requesting deferral."
+ "I40@0:8^{__SecTrust=}16@24@32"
+ "IMAPSearchIndexer/IndexingStatistics.swift"
+ "MFServerSSLAllowsTrustPrompt"
+ "MFServerSSLCertificateIsTrusted"
+ "No active request {%!l(MISSING)d}."
+ "OS_sec_protocol_metadata"
+ "OS_sec_trust"
+ "Refusing download & index due to low disk space %!{(MISSING)iec-bytes}ld / %!{(MISSING)iec-bytes}ld."
+ "Request #%!u(MISSING) {%!l(MISSING)d}, running for %!{(MISSING)public}s"
+ "Resource values for volume '%!{(MISSING)public}s'. are out of bounds: %!l(MISSING)d %!l(MISSING)ld."
+ "Start B {%!l(MISSING)d}"
+ "Starting batch %!l(MISSING)lu with %!l(MISSING)d items (%!s(MISSING)). Adding %!h(MISSING)u {%!s(MISSING)}. Updating %!h(MISSING)u. Deleting %!h(MISSING)u."
+ "Starting {%!l(MISSING)d} for %!l(MISSING)d account(s): %!{(MISSING)public}s"
+ "Stop {%!l(MISSING)d}"
+ "Sync did complete. No un-indexed messages."
+ "Sync did complete. Still %!l(MISSING)d un-indexed message(s)."
+ "Sync did defer."
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] (Re-)enqueuing (deferred) message request %!s(MISSING) due to batch size limits."
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] Currently no capacity for deferred message request %!s(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] Enqueuing message request %!s(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] No deferred message requests."
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] Popped deferred message request %!s(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] Returning %!l(MISSING)d messages for request %!s(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Another certificate has already been trusted. Failing on certificate change."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Authentication completed (took %!l(MISSING)d s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Authentication completed with server %!{(MISSING)public}s (took %!l(MISSING)d s)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Connection security does not fulfil requirements for sending credentials."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Failed to save account."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Failed to save account: %!@(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Fatal trust failure."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Got %!u(MISSING) from CertUI."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] SecTrustEvaluateAsyncWithError() completed with error: %!@(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] SecTrustEvaluateAsyncWithError() failed."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sending credentials over insecure connection (opportunistic TLS)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sending credentials over insecure connection."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] TLS policy not met."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Trust denied."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Trust evaluation failed with other error."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Trust evaluation failed."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Unable to get account."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Unspecified trust result."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] User (previously) denied untrusted certificate(s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] We ran STARTTLS, but the connection is not secure."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Using fixed range(s): %!{(MISSING)public}s (batch size: %!l(MISSING)d)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query local persistence (message count: %!l(MISSING)d, batch size: %!l(MISSING)d)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query server. (batch size: %!l(MISSING)d)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing unknown messages in range #%!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [Prompt] Prompting user about untrusted certificate(s) (allowTrust: %!{(MISSING)BOOL}d)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [Prompt] User allowed untrusted certificate(s) for session."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [Prompt] User allowed untrusted certificate(s) permanently."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [Prompt] User denied untrusted certificate(s)."
+ "[%!l(MISSING)lu] Failed to send indexing stats to maild: %!@(MISSING)"
+ "[%!l(MISSING)lu] Sending indexing stats to maild."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Download & index did complete."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Download & index did defer work."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Download & index did not complete."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Starting download & index."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Stopping download & index, but not in downloading state."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Stopping download & index."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Trying to start download & index, but already running."
+ "_TtC12IMAP2Helpers12CertUIPrompt"
+ "_TtC12IMAP2Helpers18CertUITrustManager"
+ "_TtCVE15IMAP2ConnectionO16IMAP2Persistence16CertificateTrust29DefaultVerifierImplementationP33_F342119D05A6F1A070C6FAB1999158A515AccountAndStore"
+ "_allow"
+ "_rawTrust"
+ "_setHostname"
+ "_setService"
+ "_setTrust"
+ "_show"
+ "_updateIndexingStatistics"
+ "accountPropertyForKey:"
+ "accountWithIdentifier:"
+ "allowCertificateTrust"
+ "allowTrust:forHost:service:"
+ "allowUserOverride"
+ "boolValue"
+ "com.apple.imap.cert-trust-verifier"
+ "endpoint"
+ "expressionForFunction:arguments:"
+ "expressionForKeyPath:"
+ "expressionResultType"
+ "failedToRenameMailboxOnServer"
+ "implementation"
+ "indexingStatisticsUpdate"
+ "isDirty"
+ "kCertUIServiceTypeIMAP"
+ "lastIndexStatsUpdate"
+ "networkAccountIdentifier"
+ "policy"
+ "rawTrustResultForSSLTrust:hostname:service:"
+ "requireTrustedTLS12"
+ "requireTrustedTLS13"
+ "saveVerifiedAccount:withCompletionHandler:"
+ "setAccountProperty:forKey:"
+ "setExpression:"
+ "setExpressionResultType:"
+ "setHost:"
+ "setPropertiesToGroupBy:"
+ "setService:"
+ "setTrust:"
+ "showPromptWithOptions:responseBlock:"
+ "store"
+ "unauthenticatedTimer"
+ "v12@?0I8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8^{__SecTrust=}16"
+ "v28@?0^{__SecTrust=}8B16^{__CFError=}20"
+ "v40@0:8^{__SecTrust=}16@24@32"
+ "{%!l(MISSING)d} %!l(MISSING)d of %!l(MISSING)d (%!l(MISSING)d%) messages are indexed."
+ "{%!l(MISSING)d} Checking current batch: request #%!u(MISSING)."
+ "{%!l(MISSING)d} Creating instance for account %!{(MISSING)public}s for request #%!u(MISSING)"
+ "{%!l(MISSING)d} Index queue did drain."
+ "{%!l(MISSING)d} Waiting for index queue to have drained."
- "\x01\x02\x03\x04\x05\x06\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x1c\x1d\x1f\x18\x19\x1a\x1b\x1e !\"#$%!&(MISSING)'("
- "Available disk space changed. Opportunistic: %!{(MISSING)iec-bytes}ld, important: %!{(MISSING)iec-bytes}ld"
- "Checking current batch: no current request."
- "Checking current batch: request #%!u(MISSING)."
- "Creating instance for account %!{(MISSING)public}s for request #%!u(MISSING)"
- "IMAPSearchIndexer/MessageLookup.swift"
- "Index queue did drain."
- "No active request."
- "NotifyMessagesVanished"
- "Refusing download & index due to low disk space %!{(MISSING)iec-bytes}ld."
- "Request #%!u(MISSING), running for %!{(MISSING)public}s"
- "Starting batch %!l(MISSING)lu with %!l(MISSING)d items (%!s(MISSING))."
- "Starting for %!l(MISSING)d account(s): %!{(MISSING)public}s"
- "Waiting for index queue to have drained."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Authentication completed with server %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Authentication completed."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] No credentials are allowed given the connection security."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Only %!l(MISSING)d of %!l(MISSING)d credential(s) are allowed given the connection security."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] We ran STARTTLS, but the connection is not secure: %!h(MISSING)u."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Using fixed range(s): %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query local persistence (message count: %!l(MISSING)d)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query server."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d messages in range #%!l(MISSING)d."
- "[%!l(MISSING)lu] Cancel -> stopping download & index."
- "[%!l(MISSING)lu] Download & index did complete."
- "[%!l(MISSING)lu] Download & index did defer work."
- "[%!l(MISSING)lu] Starting download & index."
- "[%!l(MISSING)lu] Stopping download & index."
- "[%!l(MISSING)lu] Trying to start download & index, but already running."
- "[%!l(MISSING)lu] Trying to stop download & index, but not running."
- "plaintextIsAllowed"

```
