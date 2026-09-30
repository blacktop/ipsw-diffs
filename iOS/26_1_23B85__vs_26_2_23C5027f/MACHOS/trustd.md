## trustd

> `/usr/libexec/trustd`

```diff

-61901.40.77.0.0
-  __TEXT.__text: 0x6034c
-  __TEXT.__auth_stubs: 0x23d0
+61901.60.29.0.0
+  __TEXT.__text: 0x63038
+  __TEXT.__auth_stubs: 0x2410
   __TEXT.__objc_stubs: 0x2dc0
   __TEXT.__objc_methlist: 0xc2c
   __TEXT.__const: 0x5c81
-  __TEXT.__gcc_except_tab: 0xc98
-  __TEXT.__cstring: 0x68e5
-  __TEXT.__oslogstring: 0x5afc
+  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__cstring: 0x701d
+  __TEXT.__oslogstring: 0x5fad
   __TEXT.__objc_classname: 0x194
   __TEXT.__objc_methname: 0x2cc0
   __TEXT.__objc_methtype: 0xaf6
-  __TEXT.__unwind_info: 0x1070
-  __DATA_CONST.__auth_got: 0x11f8
+  __TEXT.__unwind_info: 0x10a8
+  __DATA_CONST.__auth_got: 0x1218
   __DATA_CONST.__got: 0x798
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x4a10
-  __DATA_CONST.__cfstring: 0x60c0
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x4c48
+  __DATA_CONST.__cfstring: 0x63c0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x4f0
+  __DATA.__bss: 0x510
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SwiftCRLite.framework/SwiftCRLite
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9B3771BA-D8AB-35A6-8785-1C884DDAA411
-  Functions: 1252
-  Symbols:   833
-  CStrings:  2966
+  UUID: 3693330E-9F45-3ADC-B600-ED3BE5F5035A
+  Functions: 1274
+  Symbols:   838
+  CStrings:  3041
 
Symbols:
+ _SecCRLiteCertStatus
+ _SecCRLiteCreate
+ _SecCRLiteDestroy
+ _SecCRLiteGetCoverageInfo
+ _SecCRLiteLoadFilter
CStrings:
+ "CREATE TABLE IF NOT EXISTS admin(key TEXT PRIMARY KEY NOT NULL,ival INTEGER NOT NULL,value BLOB);CREATE TABLE IF NOT EXISTS issuers(groupid INTEGER NOT NULL,issuer_hash BLOB PRIMARY KEY NOT NULL);CREATE INDEX IF NOT EXISTS issuer_idx ON issuers(issuer_hash);CREATE TABLE IF NOT EXISTS groups(groupid INTEGER PRIMARY KEY AUTOINCREMENT,flags INTEGER,format INTEGER,data BLOB,policies BLOB);CREATE TABLE IF NOT EXISTS serials(groupid INTEGER NOT NULL,serial BLOB NOT NULL,UNIQUE(groupid,serial));CREATE TABLE IF NOT EXISTS hashes(groupid INTEGER NOT NULL,sha256 BLOB NOT NULL,UNIQUE(groupid,sha256));CREATE TABLE IF NOT EXISTS dates(groupid INTEGER PRIMARY KEY NOT NULL,notbefore REAL,notafter REAL);CREATE TABLE IF NOT EXISTS crlitefilters(filterid INTEGER PRIMARY KEY NOT NULL,filterversion INTEGER,data BLOB);CREATE TABLE IF NOT EXISTS crlitefiltercoverage(filterid INTEGER NOT NULL,logid BLOB NOT NULL,generatedat REAL,start REAL,end REAL,UNIQUE(filterid,logid));CREATE TRIGGER IF NOT EXISTS group_del BEFORE DELETE ON groups FOR EACH ROW BEGIN DELETE FROM serials WHERE groupid=OLD.groupid; DELETE FROM hashes WHERE groupid=OLD.groupid; DELETE FROM issuers WHERE groupid=OLD.groupid; DELETE FROM dates WHERE groupid=OLD.groupid; END;"
+ "CRLite section trailing bytes exceed remaining buffer"
+ "CRLiteGenerationUsed"
+ "CRLiteUsed"
+ "CRLiteVersionUsed"
+ "DELETE FROM crlitefiltercoverage; DELETE FROM crlitefilters;"
+ "DELETE FROM groups; DELETE FROM crlitefiltercoverage; DELETE FROM crlitefilters;DELETE FROM admin WHERE key='version'; DELETE FROM sqlite_sequence"
+ "Failed to deserialize CRLite filter metadata for filter %u of %u"
+ "Failed to evaluate CRLite certificate revocation status against filter %ld: %@"
+ "Failed to extract SCT logID and timestamp"
+ "Failed to get CRLite filter data for filter %ld: %@"
+ "Failed to get CRLite filter data: %@"
+ "Failed to ingest CRLite filter for filter %u of %u"
+ "Failed to load CRLite filter: %@"
+ "Failed to parse CRLite filter metadata for filter %u of %u"
+ "INSERT INTO crlitefiltercoverage (filterid,logid,generatedat,start,end) VALUES (?,?,?,?,?)"
+ "INSERT INTO crlitefilters (filterversion,data) VALUES (?,?)"
+ "Invalid filter version in metadata; expected: %ld, got: %ld"
+ "SELECT * FROM crlitefiltercoverage WHERE logid=?1 AND ?2 >= start AND ?2 <= end ORDER BY generatedat DESC LIMIT 1"
+ "SELECT data FROM crlitefilters WHERE filterid=?"
+ "SecCRLiteInfo"
+ "SecRevocationDbIngestCRLiteUpdate failed: %@"
+ "SecValidUpdateProcessCRLiteSection: CRLite section overrun"
+ "SecValidUpdateProcessCRLiteSection: failed to clear CRLite database due to fullCRLiteUpdate"
+ "SecValidUpdateProcessCRLiteSection: failed to ingest CRLite filter"
+ "SecValidUpdateProcessCRLiteSection: failed to parse CRLite filter metadata"
+ "SecValidUpdateProcessCRLiteSection: failed to parse overall CRLite metadata"
+ "SecValidUpdateProcessCRLiteSection: invalid CRLite filter data length"
+ "SecValidUpdateProcessCRLiteSection: invalid CRLite section length"
+ "SecValidUpdateProcessCRLiteSection: missing CRLite filter count"
+ "SecValidUpdateProcessCRLiteSection: missing CRLite filter data length"
+ "SecValidUpdateProcessCRLiteSection: missing CRLite filter metadata length"
+ "SecValidUpdateProcessCRLiteSection: missing CRLite section length"
+ "SecValidUpdateProcessCRLiteSection: missing overall CRLite metadata length"
+ "SecValidUpdateProcessData: invalid filter version in metadata"
+ "UseCRLite"
+ "_SecRevocationDbCRLiteGetMostRecentCoveringFilter failed: %@"
+ "crliteInfo<%p> isRevoked:%@ generationUsed:%u versionUsed:%u"
+ "crlitefiltercache"
+ "failed to clear CRLite database due to fullCRLiteUpdate"
+ "failed to parse overall CRLite metadata"
+ "failed to parse overall CRLite metadata (len %u, remaining %zu)"
+ "found a bad filter cache entry at %ld"
+ "fullCRLiteUpdate"
+ "generatedAt"
+ "insufficient data for CRLite filter count"
+ "insufficient data for CRLite filter data length"
+ "insufficient data for CRLite filter metadata length"
+ "insufficient data for CRLite section length"
+ "insufficient data for overall CRLite metadata length"
+ "invalid CRLite filter data length %u (remaining %zu)"
+ "invalid CRLite section length: %u (remaining %zu)"
+ "policy: too many nodes"
+ "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}^{dispatch_queue_s}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
- "CREATE TABLE IF NOT EXISTS admin(key TEXT PRIMARY KEY NOT NULL,ival INTEGER NOT NULL,value BLOB);CREATE TABLE IF NOT EXISTS issuers(groupid INTEGER NOT NULL,issuer_hash BLOB PRIMARY KEY NOT NULL);CREATE INDEX IF NOT EXISTS issuer_idx ON issuers(issuer_hash);CREATE TABLE IF NOT EXISTS groups(groupid INTEGER PRIMARY KEY AUTOINCREMENT,flags INTEGER,format INTEGER,data BLOB,policies BLOB);CREATE TABLE IF NOT EXISTS serials(groupid INTEGER NOT NULL,serial BLOB NOT NULL,UNIQUE(groupid,serial));CREATE TABLE IF NOT EXISTS hashes(groupid INTEGER NOT NULL,sha256 BLOB NOT NULL,UNIQUE(groupid,sha256));CREATE TABLE IF NOT EXISTS dates(groupid INTEGER PRIMARY KEY NOT NULL,notbefore REAL,notafter REAL);CREATE TRIGGER IF NOT EXISTS group_del BEFORE DELETE ON groups FOR EACH ROW BEGIN DELETE FROM serials WHERE groupid=OLD.groupid; DELETE FROM hashes WHERE groupid=OLD.groupid; DELETE FROM issuers WHERE groupid=OLD.groupid; DELETE FROM dates WHERE groupid=OLD.groupid; END;"
- "DELETE FROM groups; DELETE FROM admin WHERE key='version'; DELETE FROM sqlite_sequence"
- "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}^{dispatch_queue_s}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"

```
