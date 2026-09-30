## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-  __TEXT.__text: 0x89034
-  __TEXT.__auth_stubs: 0x15e0
+  __TEXT.__text: 0x8b3bc
+  __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x22c
   __TEXT.__const: 0x2d5
-  __TEXT.__cstring: 0x8914
-  __TEXT.__oslogstring: 0x13763
+  __TEXT.__cstring: 0x8e75
+  __TEXT.__oslogstring: 0x1411d
   __TEXT.__objc_methname: 0x506
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methtype: 0x237
-  __TEXT.__unwind_info: 0x630
+  __TEXT.__unwind_info: 0x638
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x958
   __DATA_CONST.__cfstring: 0x140

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0xaf8
+  __DATA_CONST.__auth_got: 0xb00
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x2d0

   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 487
-  Symbols:   1218
-  CStrings:  2657
+  Functions: 489
+  Symbols:   1221
+  CStrings:  2708
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _dnssd_hints_find_host_name_conflict
+ _dnssd_hints_finish_name_conflict_check
+ _sqlite3_bind_blob
CStrings:
+ "%{public}s: %{private, mask.hash}s has %d messages in the database, not saving any more."
+ "%{public}s: %{public}s %{private, mask.hash}s with key tag %x conflicts with existing %u second key lease on key tag %x expiring at %{public}s"
+ "%{public}s: %{public}s lease query failed: %d%{public}s"
+ "%{public}s: data already present for %{private, mask.hash}s %x/%x"
+ "%{public}s: failed to consume sandbox token: %s"
+ "%{public}s: insert failed for %{private, mask.hash}s %x/%x with unexpected error %d"
+ "%{public}s: successfully consumed sandbox token"
+ "%{public}s: successfully inserted instance for %{private, mask.hash}s %x/%x"
+ "%{public}s: successfully inserted lease for %x/%x"
+ "%{public}s: successfully inserted message for %x/%x"
+ "%{public}s: successfully updated instance for %{private, mask.hash}s %x/%x"
+ "%{public}s: successfully updated lease for %x/%x: %d"
+ "%{public}s: successfully updated message receive_time for %x/%x: %d"
+ "%{public}s: unable to bind instance hint: %d %{public}s"
+ "%{public}s: unable to bind instance instance_name: %d %{public}s"
+ "%{public}s: unable to bind instance key_tag: %d %{public}s"
+ "%{public}s: unable to bind lease update column %d key_tag: %d %{public}s"
+ "%{public}s: unable to bind message blob: %d %{public}s"
+ "%{public}s: unable to bind message hint: %d %{public}s"
+ "%{public}s: unable to bind message hostname: %d %{public}s"
+ "%{public}s: unable to bind message key_tag: %d %{public}s"
+ "%{public}s: unable to bind message prefix: %d %{public}s"
+ "%{public}s: unable to bind message removes_all: %d %{public}s"
+ "%{public}s: unable to bind message update column %d key_tag: %d %{public}s"
+ "%{public}s: unable to fetch message count for %{private, mask.hash}s: %d %{public}s"
+ "%{public}s: unable to insert lease %x/%x: %d %{public}s"
+ "%{public}s: unable to insert message: %d %{public}s"
+ "%{public}s: unable to prepare the instance insert statement: %d%{public}s"
+ "%{public}s: unable to prepare the instance update statement: %d%{public}s"
+ "%{public}s: unable to prepare the leases insert statement: %d: %{public}s"
+ "%{public}s: unable to prepare the leases update statement: %d%{public}s"
+ "%{public}s: unable to prepare the message count statement: %d: %{public}s"
+ "%{public}s: unable to prepare the messages insert statement: %d: %{public}s"
+ "%{public}s: unable to prepare the messages update statement: %d%{public}s"
+ "%{public}s: unable to update lease %x/%x: %d %{public}s"
+ "%{public}s: unable to update message %x/%x: %d %{public}s"
+ "%{public}s: update failed for %{private, mask.hash}s %x/%x with unexpected error %d"
+ "00:32:02"
+ "INSERT INTO instances(name, key_tag, hint, prefix) VALUES (?, ?, ?, ?);"
+ "INSERT INTO leases(host_expiry, key_expiry, receive_time, key_tag, hint) VALUES (?, ?, ?, ?, ?);"
+ "INSERT INTO messages(key_tag, hint, message, removes_all, hostname) VALUES (?, ?, ?, ?, ?);"
+ "Jun 25 2026"
+ "SELECT COUNT(hint) from messages WHERE key_tag = ?;"
+ "SELECT leases.key_tag, leases.receive_time, leases.key_expiry FROM leases, messages WHERE leases.key_expiry + leases.receive_time > ?   AND message.hostname = ?   AND key_tag != ?   AND leases.key_tag = message.key_tag AND leases.hint = message.hint ORDER BY leases.key_expiry + leases.receive_time DESC LIMIT 1"
+ "SELECT leases.key_tag, leases.receive_time, leases.key_lease FROM leases, instances WHERE leases.key_expiry + leases.receive_time > ?   AND instances.name = ?   AND key_tag != ?   AND leases.key_tag = instances.key_tag AND leases.hint = instances.hint ORDER BY leases.receive_time + leases.key_lease DESC LIMIT 1"
+ "UPDATE instances SET key_tag = ?, hint = ? WHERE name = ? and prefix = ?;"
+ "UPDATE leases SET host_expiry = ?, key_expiry = ?, receive_time = ? WHERE key_tag = ? AND hint = ?;"
+ "UPDATE messages SET receive_time = ? WHERE key_tag = ? AND hint = ?;"
+ "dnssd_hints_find_host_name_conflict"
+ "dnssd_hints_find_instance_name_conflict"
+ "dnssd_hints_finish_name_conflict_check"
+ "dnssd_hints_sqlite_instance_to_message_map_add"
+ "dnssd_hints_sqlite_message_update"
- "22:13:39"
- "Jun  9 2026"

```
