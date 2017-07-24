# -*- mode: python -*-

block_cipher = None


a = Analysis(['server.py'],
             pathex=['c:\\python27\\Lib\\site-packages\\eventlet\\support', 'c:\\python27\\Lib\\site-packages\\dxlclient\\_vendor', '.\\'],
             binaries=[],
             datas=[('logs', 'logs'), ('dxlclient.config', '.'), ('*.crt', '.'), ('*.key', '.')],
             hiddenimports=['dns.dnssec', 'dns.exception', 'dns.e164', 'dns.namedict', 'dns.tsigkeyring', 'dns.ttl', 'dns.zone', 'dns.update', 'dns.edns', 'dns.entropy', 'dns.exception', 'dns.flags', 'dns.grange','dns.hash', 'dns.inet', 'dns.ipv4', 'dns.ipv6', 'dns.message', 'dns.name', 'dns.node', 'dns.opcode', 'dns.query', 'dns.rcode', 'dns.rdata', 'dns.rdataclass', 'dns.rdataset', 'dns.rdatatype', 'dns.renderer', 'dns.resolver', 'dns.reversename', 'dns.rrset', 'dns.set', 'dns.tsig', 'dns.version', 'dns.wiredata', 'dns.zone', 'msgpack'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='server',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='server')
