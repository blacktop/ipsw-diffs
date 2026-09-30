## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.82.1.0.0
-  __TEXT.__text: 0x170994
-  __TEXT.__auth_stubs: 0x3d90
-  __TEXT.__objc_methlist: 0x5308
-  __TEXT.__const: 0xa5f0
-  __TEXT.__cstring: 0x179aa
-  __TEXT.__gcc_except_tab: 0x8d38
-  __TEXT.__oslogstring: 0xedc1
+61439.100.301.0.0
+  __TEXT.__text: 0x172b68
+  __TEXT.__auth_stubs: 0x3e50
+  __TEXT.__objc_methlist: 0x5fd8
+  __TEXT.__const: 0xa3e8
   __TEXT.__dlopen_cstrs: 0x359
+  __TEXT.__cstring: 0x17d66
+  __TEXT.__gcc_except_tab: 0x8bfc
+  __TEXT.__oslogstring: 0xef8b
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5f18
-  __TEXT.__objc_classname: 0xadd
-  __TEXT.__objc_methname: 0xb655
-  __TEXT.__objc_methtype: 0x34b7
-  __TEXT.__objc_stubs: 0x8800
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x11cf0
+  __TEXT.__unwind_info: 0x5d80
+  __TEXT.__objc_classname: 0xae3
+  __TEXT.__objc_methname: 0xb894
+  __TEXT.__objc_methtype: 0x354a
+  __TEXT.__objc_stubs: 0x8920
+  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__const: 0x11d68
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f60
+  __DATA_CONST.__objc_selrefs: 0x30c0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x2c0
-  __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x1ee0
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x4360
-  __AUTH_CONST.__cfstring: 0x152e0
-  __AUTH_CONST.__objc_const: 0xae00
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_arraydata: 0x100
+  __AUTH_CONST.__auth_got: 0x1f40
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x4320
+  __AUTH_CONST.__cfstring: 0x158c0
+  __AUTH_CONST.__objc_const: 0x98f8
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1d10
-  __AUTH.__data: 0xd10
+  __AUTH.__data: 0xd28
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x48
-  __DATA.__objc_ivar: 0x5bc
-  __DATA.__data: 0x20c0
-  __DATA.__bss: 0x9f0
+  __DATA.__objc_ivar: 0x5e4
+  __DATA.__data: 0x20e0
+  __DATA.__bss: 0xa00
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x40

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6818
-  Symbols:   9412
-  CStrings:  8088
+  Functions: 6801
+  Symbols:   9520
+  CStrings:  8175
 
Symbols:
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _SecCertificateCopyAnchorLookupKey
+ _SecCertificateCopyQualifiedCertificateStatements
+ _SecPolicyCreate3PMobileAsset
+ _SecPolicyCreateQWAC
+ _SecPolicyGetCompatibilityOidString
+ _SecPolicyUsesAppleAnchors
+ _SecPolicyUsesConstrainedAnchors
+ _SecTrustStoreCopyAnchors
+ _aks_assert_drop
+ _aks_assert_hold
+ _aks_create_bag
+ _aks_get_lock_state
+ _aks_load_bag
+ _aks_save_bag
+ _aks_unload_bag
+ _aks_unlock_bag
+ _ccscrypt
+ _ccscrypt_storage_size
+ _ccspake_cp_256_rfc
+ _ccspake_generate_L
+ _ccspake_reduce_w
+ _ccspake_sizeof_point
+ _ccspake_sizeof_w
+ _inet_pton
+ _kCFPreferencesAnyUser
+ _kSecPolicyApple3PMobileAsset
+ _kSecPolicyAppleEAPClient
+ _kSecPolicyAppleEAPServer
+ _kSecPolicyAppleIPSecClient
+ _kSecPolicyAppleIPSecServer
+ _kSecPolicyAppleQWAC
+ _kSecPolicyAppleSSLClient
+ _kSecPolicyAppleSSLServer
+ _kSecPolicyCheckQWAC
+ _kSecPolicyNameAppleIssuedTransparent
+ _kSecQCStatementCompliance
+ _kSecQCStatementType
+ _kSecQCStatementTypeEseal
+ _kSecQCStatementTypeEsign
+ _kSecQCStatementTypeWeb
+ _kSecSFAErrorDomain
+ _kSecTrustInfoQCStatementsKey
+ _kSecTrustInfoQWACValidationKey
+ _kSecTrustQCStatements
+ _kSecTrustQWACValidation
+ _objc_retainAutoreleasedReturnValue
+ _sec_identity_copy_SPAKE2PLUSV1_client_identity
+ _sec_identity_copy_SPAKE2PLUSV1_client_password_verifier
+ _sec_identity_copy_SPAKE2PLUSV1_context
+ _sec_identity_copy_SPAKE2PLUSV1_registration_record
+ _sec_identity_copy_SPAKE2PLUSV1_server_identity
+ _sec_identity_copy_SPAKE2PLUSV1_server_password_verifier
+ _sec_identity_copy_type
+ _sec_identity_create_SPAKE2PLUSV1_client_password_verifier
+ _sec_identity_create_SPAKE2PLUSV1_registration_record
+ _sec_identity_create_SPAKE2PLUSV1_server_password_verifier
+ _sec_identity_create_client_SPAKE2PLUSV1_identity
+ _sec_identity_create_server_SPAKE2PLUSV1_identity
+ _sec_protocol_configuration_copy_transformed_options_for_address
+ _sec_protocol_metadata_get_tls_negotiated_pake
+ _sec_protocol_options_get_pqtls_mode
+ _sec_protocol_options_set_pqtls_mode
+ _sec_protocol_options_set_sec_protocol_configuration
- _IOConnectCallMethod
- _IOServiceClose
- _IOServiceMatching
- _IOServiceOpen
- _OBJC_CLASS_$_NSMutableCharacterSet
- ___stdoutp
- _calloc
- _kIOMasterPortDefault
CStrings:
+ "\x01\x12"
+ "\t"
+ "#\x16"
+ "%@\n%@\nRelated radar: rdar://%@\nRequest triggered at: %@"
+ "%d zero read (ignored)"
+ "/System/AppleInternal/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit"
+ "/System/AppleInternal/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"
+ "1.2.840.113635.100.1.11.1"
+ "1.2.840.113635.100.1.11.2"
+ "1.2.840.113635.100.1.120"
+ "1.2.840.113635.100.1.122"
+ "1.2.840.113635.100.1.3.1"
+ "1.2.840.113635.100.1.3.2"
+ "1.2.840.113635.100.1.9.1"
+ "1.2.840.113635.100.1.9.2"
+ "1.2.840.113635.100.6.2.13"
+ "1.2.840.113635.100.6.30"
+ "1.3.6.1.5.5.7.3.36"
+ "3PMobileAsset"
+ "@\"NSObject<OS_dispatch_data>\""
+ "@32@0:8q16@24"
+ "@40@0:8q16@24@32"
+ "AllowAllMetrics"
+ "App Transport Security exception %{public}@ is not a valid CIDR notation."
+ "AppleIssuedTransparent"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "B32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8"
+ "B44@0:8i16@20@28^@36"
+ "CREATE TABLE IF NOT EXISTS hard_failures (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,data BLOB\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_hard_failures;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_hard_failures_v2 AFTER INSERT ON hard_failures\nBEGIN\nDELETE FROM hard_failures WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS soft_failures (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,data BLOB\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_soft_failures;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_soft_failures_v2 AFTER INSERT ON soft_failures\nBEGIN\nDELETE FROM soft_failures WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS notes (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,data BLOB\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_notes;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_notes_v2 AFTER INSERT ON notes\nBEGIN\nDELETE FROM notes WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS samples (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,\nname STRING,\nvalue REAL\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_samples;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_samples_v2 AFTER INSERT ON samples\nBEGIN\nDELETE FROM samples WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS success_count (\nevent_type STRING PRIMARY KEY,\nsuccess_count INTEGER,\nhard_failure_count INTEGER,\nsoft_failure_count INTEGER\n);\nCREATE TABLE IF NOT EXISTS rockwell (\nevent_type STRING PRIMARY KEY,\ntimestamp REAL,data BLOB\n);\nCREATE TABLE IF NOT EXISTS upload_file (\nfile STRING PRIMARY KEY,\nstore STRING,\ntimestamp REAL\n);\nDROP TABLE IF EXISTS all_events;\n"
+ "Certificate is not a qualified web certificate"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Couldn't fetch initial sync status for view %@: %@"
+ "Couldn't json validate rockwell record: %@"
+ "Couldn't serialize json record: %@"
+ "Couldn't serialize rockwell record: %@"
+ "Couldn't validate json record: %@"
+ "Crash/Hang/Data Loss"
+ "Description"
+ "EnableAppTransportSecurityAppleBundleException"
+ "Failed to create notification, error %@"
+ "Initial sync completed for view %@: %{BOOL}d"
+ "Invalid QCS Type"
+ "Invalid QCStatements Extension"
+ "JSON:%@"
+ "NSCIDRExceptions"
+ "NSParsedCIDRAddressKey"
+ "NSParsedCIDRMaskKey"
+ "NSParsedCIDRPrefixKey"
+ "NSString *getkSecurityRTCEventNameEstablish(void)"
+ "No rules, not setting up collection"
+ "Not Applicable"
+ "QCSCompliance"
+ "QCSType"
+ "QCSTypeEseal"
+ "QCSTypeEsign"
+ "QCSTypeWeb"
+ "QCStatements"
+ "QWAC"
+ "QWACValidation"
+ "Qualified Certificate"
+ "Qualified Certificate Statements"
+ "Qualified Certificate Type"
+ "Reproducibility"
+ "SecTrustStoreCopyAnchors"
+ "StringAsConfigVersion:"
+ "T@\"NSDate\",&,V_created"
+ "Ti,N,V_configVersion"
+ "Title"
+ "TrustQCStatements"
+ "TrustQWACValidation"
+ "VerifiedMark"
+ "_AsyncPiperForTestingFailPipe"
+ "_AsyncPiperForTestingFailXpcFdWrapping"
+ "_configVersion"
+ "_created"
+ "base version"
+ "client_identity"
+ "client_password_verifier"
+ "configVersion"
+ "configVersion missing"
+ "configVersion not understood %@, this tool knows about %d"
+ "configVersionAsString:"
+ "created"
+ "databaseBasename"
+ "dlsym libnetwork nw_protocol_options_copy"
+ "errorWithCode:description:"
+ "errorWithCode:description:underlying:"
+ "establish:error:"
+ "hasConfigVersion"
+ "initWithName:value:"
+ "initWithSPAKE2PLUSV1Context:clientIdentity:serverIdentity:clientPasswordVerifier:serverPasswordVerifier:registrationRecord:"
+ "initialSyncStatus:reply:"
+ "isVersionSameOrNewer:than:"
+ "kSecurityRTCEventNameEstablish"
+ "logRockwellFailureForEventNamed:withAttributes:"
+ "mediaplaybackd"
+ "nw_protocol_options_copy"
+ "openSensitiveURL:withOptions:"
+ "parseVersions:error:"
+ "pathExtension"
+ "pqtls_mode"
+ "queryItems"
+ "rangeOfString:"
+ "registration_record"
+ "requiredVersion:rules:reason:error:"
+ "rules config format version %d because %@"
+ "server_identity"
+ "server_password_verifier"
+ "setConfigVersion:"
+ "setCreated:"
+ "setHasConfigVersion:"
+ "setQueryItems:"
+ "spake2_context"
+ "streamEventsWithLimit:fromTable:eventHandler:"
+ "tap-to-radar://new"
+ "timestamp DESC"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v52@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8I16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}20^v44"
+ "version1"
+ "version2"
+ "versions is string: %@"
+ "versions on rule"
+ "visionOS"
+ "{?=\"configVersion\"b1}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}24@?0r^v8r^v16"
- "\b"
- "\"AllowAllMetrics\""
- "\"Security\""
- "%@\n%@\nRelated radar: rdar://%@"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "&"
- ".."
- "AppleKeyStore"
- "AsyncPiperFailPipeForTesting"
- "AsyncPiperFailXpcFdWrappingForTesting"
- "B32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8"
- "CREATE TABLE IF NOT EXISTS hard_failures (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,data BLOB\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_hard_failures;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_hard_failures_v2 AFTER INSERT ON hard_failures\nBEGIN\nDELETE FROM hard_failures WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS soft_failures (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,data BLOB\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_soft_failures;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_soft_failures_v2 AFTER INSERT ON soft_failures\nBEGIN\nDELETE FROM soft_failures WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS notes (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,data BLOB\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_notes;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_notes_v2 AFTER INSERT ON notes\nBEGIN\nDELETE FROM notes WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS samples (\nid INTEGER PRIMARY KEY AUTOINCREMENT,\ntimestamp REAL,\nname STRING,\nvalue REAL\n);\nDROP TRIGGER IF EXISTS maintain_ring_buffer_samples;\nCREATE TRIGGER IF NOT EXISTS maintain_ring_buffer_samples_v2 AFTER INSERT ON samples\nBEGIN\nDELETE FROM samples WHERE id <= NEW.id - 1000;\nEND;\nCREATE TABLE IF NOT EXISTS success_count (\nevent_type STRING PRIMARY KEY,\nsuccess_count INTEGER,\nhard_failure_count INTEGER,\nsoft_failure_count INTEGER\n);\nCREATE TABLE IF NOT EXISTS rockwell (\nevent_type STRING PRIMARY KEY,\ntimestamp REAL,data BLOB\n);\nDROP TABLE IF EXISTS all_events;\n"
- "Couldn't serialize failure record: %@"
- "Failed to create notification error %@"
- "IOService:/IOResources/AppleKeyStore"
- "Test Apple System Integration CA - ECC"
- "URLQueryAllowedCharacterSet"
- "URLWithString:"
- "WORKSTATION"
- "_create_bag"
- "`\x86H\x01\x86\xf8E\x01\t"
- "aks"
- "aks-client-queue"
- "aks_assert_drop"
- "aks_assert_hold"
- "aks_get_lock_state"
- "aks_load_bag"
- "aks_save_bag"
- "aks_unload_bag"
- "aks_unlock_bag"
- "errorWithDomain:code:description:underlying:"
- "failed to open connection to %s\n"
- "formUnionWithCharacterSet:"
- "matchRuleWithSelf:"
- "mediaserverd"
- "openURL:configuration:completionHandler:"
- "parseVersions:format:error:"
- "removeCharactersInString:"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "tap-to-radar://new?Title=%@&ComponentName=%@&ComponentVersion=%@&Reproducibility=Not%%20Applicable&ComponentID=%@&Classification=Crash/Hang/Data%%20Loss&Description=%@"
- "v52@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8I16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}20^v44"
- "versions it string: %@"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}24@?0r^v8r^v16"

```
