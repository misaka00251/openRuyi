# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: Maybe we need to remove this for licensing reasons
%bcond fdk_aac 0

# TODO: Official branding is tricky
# https://www.mozilla.org/en-US/foundation/trademarks/policy/
%bcond official_branding 0

Name:           firefox
Version:        158.0.1
Release:        %autorelease
Summary:        Free web browser backed by Mozilla
License:        MPL-2.0
URL:            https://www.firefox.com
# https://bugzilla.mozilla.org/show_bug.cgi?id=1863519
VCS:            git:https://github.com/mozilla-firefox/firefox
#!RemoteAsset:  sha256:b5beff55fa73a29a674a867da5922f5d7699f51e351e6bbe4405fcc4ba55a824
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# We need the language packs
#!RemoteAsset:  sha256:8e8a3da8715336bbeb7a8fc4550dfd12208c1c5662f34805c298ea74a2f6b984
Source1:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ach.xpi
#!RemoteAsset:  sha256:963793c492693b18fc58bfe20d381f090a1c9b42ef9efed71ae6931226c3cecb
Source2:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/af.xpi
#!RemoteAsset:  sha256:86a160be4ebaa78167ca2de3057f5efa856238ba5449990d8635821be9e54027
Source3:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/an.xpi
#!RemoteAsset:  sha256:9b92ec5a69c56f676b2ef8e7d95d172c656837b342e0156a558c3f615fe1935e
Source4:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ar.xpi
#!RemoteAsset:  sha256:8e28ca0c222184c24780779af1ff42025a8ec0b50531d0d7383b1955d83917ed
Source5:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ast.xpi
#!RemoteAsset:  sha256:974e41a45c07210c55a9c0e6e94acc59af52541ee926c60c57a472f11e015838
Source6:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/az.xpi
#!RemoteAsset:  sha256:a4bec0a57ba39f3958386906f35d541213290e6a47e2a1b8231514c848e9f818
Source7:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/be.xpi
#!RemoteAsset:  sha256:7c76a642c1966ed65565e04c9c603a59504b107b919cee2d535cf7d24f37636f
Source8:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bg.xpi
#!RemoteAsset:  sha256:96561e861f59330257fa93bea90d4aa7238e22e5bd8553b536928e3bfc00d1a0
Source9:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bn.xpi
#!RemoteAsset:  sha256:a39656fa8cd3af55db2ecc7d766aff37d6ba907ebdf038e2e3c50541de1fd28e
Source10:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/br.xpi
#!RemoteAsset:  sha256:289c3b218fa043bcccf09ed1cc9f9cd7d8e68c12a4099e1a8eebfad8bbe329c3
Source11:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bs.xpi
#!RemoteAsset:  sha256:fbf568fd5ed70e3a004e11455358cadeffcd96acd35af90c75cf016ff2434097
Source12:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca-valencia.xpi
#!RemoteAsset:  sha256:b35d9cd210d3c3e3dd0f7ebd5064f766305d5244cde0809dfe29c209d5e66da2
Source13:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca.xpi
#!RemoteAsset:  sha256:b98dbaee917d365e1ef45d86e32355c550ac3e6e26f39fc512d77dcd39a52b12
Source14:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cak.xpi
#!RemoteAsset:  sha256:9f2df4a0c45b78c13cb6ea517b09cdcf61b52eb81fb234a03534d3c65d0f0d7a
Source15:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cs.xpi
#!RemoteAsset:  sha256:8bbf35014e0c2f471c700397a0527f547bfec4dc3489a08caaa48c6f4e4db5c5
Source16:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cy.xpi
#!RemoteAsset:  sha256:b479ea84e8d2756eb86748e8b8a4e02ab2d782e8ee3864e433c1c25cdd467749
Source17:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/da.xpi
#!RemoteAsset:  sha256:2b7d6d0991232fe360f29c034e505e7ebe1925c4bba47960a577d5558fd6b1d5
Source18:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/de.xpi
#!RemoteAsset:  sha256:a75b6ea3fe201de81f04815c09e3a7d2b4754c92845588abaec4d7ac72ad2ec2
Source19:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/dsb.xpi
#!RemoteAsset:  sha256:395307596aceedf0a2fe1ba9bf21fb9668166aee712e13fd03ce844a2f343a8c
Source20:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/el.xpi
#!RemoteAsset:  sha256:07c237da66ac83c770d63da139d4ff72db3c641f92c52ca8443773ef7630f761
Source21:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-CA.xpi
#!RemoteAsset:  sha256:76d6698c9ff0ab55d427d41e3eb2d9cbc151a0dd5de2f890bbcf389437d076c5
Source22:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-GB.xpi
#!RemoteAsset:  sha256:603327cf7eef78b1c161dccf98d8da5fd45b2c84a46943453846fcf5ced699bb
Source23:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-US.xpi
#!RemoteAsset:  sha256:7cab63a2cb0ba1ba5f7c7ffed5417b14e9bf5f4b1d223689a930780d6c339912
Source24:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eo.xpi
#!RemoteAsset:  sha256:412fd1eca1e389c662ce81e526822ab1962b9d52213ef81e30d428188939014b
Source25:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-AR.xpi
#!RemoteAsset:  sha256:0225efa071f5b658a85d1d8f9ae77a7f95ef96e03de7f090dc74bde250868775
Source26:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-CL.xpi
#!RemoteAsset:  sha256:63281e5aef25dc2f51602793d238ede54650077b46af20d5efdf1f0838df6a0c
Source27:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-ES.xpi
#!RemoteAsset:  sha256:b5b9d84c6c2046bdd7813fe5c24a5ebb070e0d0b21f27199b7fa82241b541e93
Source28:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-MX.xpi
#!RemoteAsset:  sha256:9777f6dcc3a38970c6cc087da210ac62dcc69ba6648a147f947b8a8300e97500
Source29:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/et.xpi
#!RemoteAsset:  sha256:a3c57365798a78730707e89f351fad6349d61eca8262168d5710d3bbbe8be660
Source30:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eu.xpi
#!RemoteAsset:  sha256:746426c584843ff1d8282a6dd950d8610631902a7fc5111d0d885547572592fd
Source31:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fa.xpi
#!RemoteAsset:  sha256:7fc2f9b54a596b1449fd42e3934274a5a0c52fe26b6a3a66d6c46d1a00f21340
Source32:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ff.xpi
#!RemoteAsset:  sha256:d1cae16e5a64862e05773e8621ea0a63f21d44d727ff135ef0af03cf0c54af5d
Source33:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fi.xpi
#!RemoteAsset:  sha256:912a0e5d44646bf52293d1f601dd879b7cbd34b2a5583f19295b26d50a595046
Source34:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fr.xpi
#!RemoteAsset:  sha256:4dfb5257f070ee910612fd1e0339be01fd15fe4971b38a01d5157bd2ea44512c
Source35:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fur.xpi
#!RemoteAsset:  sha256:f1dc7c2a7b5832655b81e44e1843d81e090b19a3212834d4427879067b1c8940
Source36:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fy-NL.xpi
#!RemoteAsset:  sha256:ba9396d739d39e84505d675bc5b66f27648a0586f0e23ca05aacbab533940c34
Source37:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ga-IE.xpi
#!RemoteAsset:  sha256:800bc63a3fb38490574baf3afb2e1708c3772fd2db38ac54feb3bc9c65347563
Source38:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gd.xpi
#!RemoteAsset:  sha256:5713f81fc9a50f56d1f87111a502be45bc021cf4b49103d0b4c16e9d2ad90939
Source39:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gl.xpi
#!RemoteAsset:  sha256:f0227aec168d5e2d8d5d3336e8b7aac2aa450bf8ea97b4f26d81b331e5f16b16
Source40:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gn.xpi
#!RemoteAsset:  sha256:3a977488aa079de53de7038b60ec69517a36ad9029d78b2b7f46bcc2fa4cd634
Source41:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gu-IN.xpi
#!RemoteAsset:  sha256:e727e775de49b49a38c874f5022869c23bfed814a34150d7669341ff70b571aa
Source42:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/he.xpi
#!RemoteAsset:  sha256:15fd7dd6c69dd4f5df56c399a97fbfabca33ffd6cf0c691193c9e6e9dc6d6f37
Source43:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hi-IN.xpi
#!RemoteAsset:  sha256:fd1dc174c595b06e02e73a7590682f51aa7cba850fac7ac352c95f4e72676ca2
Source44:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hr.xpi
#!RemoteAsset:  sha256:6ad25950765fd73e422c83f55286fbf54e9cb3e6b35f93ad643d917328ffd3a4
Source45:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hsb.xpi
#!RemoteAsset:  sha256:f11d5c563c9c079e6cd0828840adf5e3b6b4a1e38fde7d91b7ac8e4cf658f101
Source46:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hu.xpi
#!RemoteAsset:  sha256:fb44fb8fbb2f9fbab655cbfd0b659cfd9c1ba950dd7f677b73d3f7a1beaf6710
Source47:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hy-AM.xpi
#!RemoteAsset:  sha256:bb89b3fc2cec35318aea96acc8a2148a12bfac3655c398a7091d2ff91b513558
Source48:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ia.xpi
#!RemoteAsset:  sha256:f71d79b276dac372f25ce759bc1eb1f810a304fe8212942df61259df7c7f4937
Source49:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/id.xpi
#!RemoteAsset:  sha256:f19a29811eca417a4e6e74c75dca8fb6286b64bdde4c2d2e3d994c2456540fba
Source50:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/is.xpi
#!RemoteAsset:  sha256:d841464f8084313e3fab21ad052cf20d3f47e2a48eb68a85c47eddaad77dc51d
Source51:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/it.xpi
#!RemoteAsset:  sha256:c0ec52326eef9b0e38ad68663326e8ad1e914b6002b6dcbaa279983add355232
Source52:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ja.xpi
#!RemoteAsset:  sha256:be7cb94fbee748208b76a3208b87dd4829add5f3f22d9666043b3ee345730947
Source53:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ka.xpi
#!RemoteAsset:  sha256:68ef4961ded440feec5797af386750f1b302d3e18bb0d001712b712b632af227
Source54:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kab.xpi
#!RemoteAsset:  sha256:bea27225eecad2eb8068716db4dacba02697bfc8a94bcb683ed55e5004b742e3
Source55:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kk.xpi
#!RemoteAsset:  sha256:9e3d05f366edec3fd4bf39d5ea267773ca734b4ecbbe926e0c0c329ab9b87491
Source56:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/km.xpi
#!RemoteAsset:  sha256:4881d610397515491ad97e5644f0202ca80b85a2afc8ed5462525deb67377479
Source57:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kn.xpi
#!RemoteAsset:  sha256:956c752a2d615a0f53cac2640a50cdcd477e60038464d92012c0efbc2a6a0526
Source58:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ko.xpi
#!RemoteAsset:  sha256:51cb2300a918fc84ca201e365a291edab59bded5a81fd02c435494e842ec5447
Source59:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lij.xpi
#!RemoteAsset:  sha256:7b9dc889692c157fc30b2aa2aec44a7cf25ae267273792f26754dbd923fba3ca
Source60:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lt.xpi
#!RemoteAsset:  sha256:055f21d170679371c425d1e4495610a5690f5e6dc5feb250e33daf16e244c671
Source61:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lv.xpi
#!RemoteAsset:  sha256:fcee599e26425707de823aefff927a320db6f5c57ef5be331a6ac3841f277aa8
Source62:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mk.xpi
#!RemoteAsset:  sha256:367d842abc272f6e5818819b14da85f77163138e5a13ae8bdd2f97af879797a5
Source63:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mr.xpi
#!RemoteAsset:  sha256:2b9316e42bafcb34e8416e0a5aed79e111736095b1318e566e079f219392b5b7
Source64:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ms.xpi
#!RemoteAsset:  sha256:f03116daadc144ea56587fe8ee80e19367bcf02782e7ffa90ab6bb051b649e4e
Source65:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/my.xpi
#!RemoteAsset:  sha256:4f3de090f15c3eb62a1d3b5bd259111af6ab4492b8132b695a38afecf2cff1b9
Source66:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nb-NO.xpi
#!RemoteAsset:  sha256:774a0b296f51385e33046e43fbf9b0ddaef7d2d930d9a5b85aec474e75a985af
Source67:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ne-NP.xpi
#!RemoteAsset:  sha256:4a96477d4f300159e3ccb825bc66d2479bfface49dbb2824b4f790de9d5ac418
Source68:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nl.xpi
#!RemoteAsset:  sha256:757640cfd70f9528d28577ae736112e87f3a4f81f8e025b15951c709ead60994
Source69:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nn-NO.xpi
#!RemoteAsset:  sha256:dd0a18cd4f5141d9a645669cab7d1fe48dd45b11e5d97a0389e38ed526c07069
Source70:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/oc.xpi
#!RemoteAsset:  sha256:5fc7ef9fb63fbcfa8661941ec679b9a0f3931b23243fd1794334ac2f02b4d7db
Source71:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pa-IN.xpi
#!RemoteAsset:  sha256:5be0e5263f92ea69775668524db58937b1e9291f6e533d6ae327105eb9a28c9f
Source72:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pl.xpi
#!RemoteAsset:  sha256:2e668c8ab6be1cb058a5e1500a23d5a1d0036a9bc5a51869573bd859f2f3423f
Source73:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-BR.xpi
#!RemoteAsset:  sha256:719cc861cfad6d49fa728971bdb28e8f5a7a8f7e78563c1fe651fccb3f49eb3a
Source74:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-PT.xpi
#!RemoteAsset:  sha256:d10b1c22c50b87753c0e6d2202c4aa87f50f1d923c558c93c16a12d9d7a642a5
Source75:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/rm.xpi
#!RemoteAsset:  sha256:27353e24613e08bc332d0e802920eef50a8a0587f69f8f80bee0fb8416fcd066
Source76:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ro.xpi
#!RemoteAsset:  sha256:df3a286cb6fd3e1cd134dacce4298d805ec2e96ba001be6aff523b14b4be6210
Source77:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ru.xpi
#!RemoteAsset:  sha256:5709f9736749b2375ced6a7cdd6f48b474cab7c50d1c42c7554f90b29fb17fea
Source78:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sat.xpi
#!RemoteAsset:  sha256:1a5cad95c4eb605f676b8908c92a4cf6f4d474a266fbf2ffbe30969138040467
Source79:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sc.xpi
#!RemoteAsset:  sha256:9521bd727775feec452043b0cae1900567cb30be75ab3d574cca6c8a2e96b15e
Source80:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sco.xpi
#!RemoteAsset:  sha256:6625c961608581edbba0edfe1ae6ef4874340cf7723558ac15b45c691bb9435e
Source81:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/si.xpi
#!RemoteAsset:  sha256:3949095f26d3b3c141426454b04541dcdf0a627e2b5107344091cb7f958c285b
Source82:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sk.xpi
#!RemoteAsset:  sha256:d8b0d6171efe89f598f5592dd3d5f56a25d20ec4e4a356c6c5ef89e15bfcbca8
Source83:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/skr.xpi
#!RemoteAsset:  sha256:4754e73ed216f455f2b459d98f4aaf93c037870dd081f6f110bb202a588c2d7c
Source84:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sl.xpi
#!RemoteAsset:  sha256:6aed89556a2ea884ab777807ca6d2956cb854e28b3a97348d7c8e95176daaf28
Source85:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/son.xpi
#!RemoteAsset:  sha256:b64eaee8f16457b2acff3d7e89b3b76d95a9972b6e849d5e6a4550fae032c77a
Source86:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sq.xpi
#!RemoteAsset:  sha256:1e48cfc530d81274747e4a003437c4490e71282c6c5a1be85885b9be8dbd9df8
Source87:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sr.xpi
#!RemoteAsset:  sha256:c3eab22a428c74a3b7dd5ae68bf64dea6170d49ff8c739f7bce0437a80056051
Source88:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sv-SE.xpi
#!RemoteAsset:  sha256:ae3bdcadec85dd21ffe97db513c63506a3897e310d9264d6016066984c9de75b
Source89:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/szl.xpi
#!RemoteAsset:  sha256:aafa28403510a67ba84c008d2a023b47d686a37f8e4c818cf625faf1c93bd014
Source90:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ta.xpi
#!RemoteAsset:  sha256:a76b1668820e6609538696cf8d973544fc5d8deca09c7504593bc6b4dac706d2
Source91:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/te.xpi
#!RemoteAsset:  sha256:95ba040a3700f14462b4fddcb54f82abe32e13909e6b06af3f19c2f22be12cd1
Source92:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tg.xpi
#!RemoteAsset:  sha256:24833c569ef68927c7362e8c1f638d6075348b07731df9f1447c488f95631f7e
Source93:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/th.xpi
#!RemoteAsset:  sha256:569399c785888722daca8dc304c57a87027b46329416c2e8a2109a8972bd9ad7
Source94:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tl.xpi
#!RemoteAsset:  sha256:9289550c8321b7f1b983abfd705321b58f0d72e69dcfd44a40b98c316d0b6dc0
Source95:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tr.xpi
#!RemoteAsset:  sha256:a131997f2ae42a929781d66be0d40375c0965e24716e135598549dc9112a7ee7
Source96:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/trs.xpi
#!RemoteAsset:  sha256:c78e474e6d67a9398857f2b0152803f7b928802ebf9b42aee624270e961ea67c
Source97:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uk.xpi
#!RemoteAsset:  sha256:07bfab67d128481b85b8ad1ff5c9787c840bbf338e6877786efcfac9b308c690
Source98:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ur.xpi
#!RemoteAsset:  sha256:55f0c4a7a35eff556ced554b0e4d2ca1ec4f9b72e23d8eec1496ed4a4e38fb88
Source99:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uz.xpi
#!RemoteAsset:  sha256:21a64fe78acd8223a13dca5c3f6dc258f2160b0cdc43458620305d671c48dc27
Source100:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/vi.xpi
#!RemoteAsset:  sha256:d85f86de0defdfb14b06d5aadf9b94ecec92be988a1c2df2c4454489203f0736
Source101:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/xh.xpi
#!RemoteAsset:  sha256:42ce6e6463b09585ae2025b8bc20e526d161125aa33272042ac96180231728ba
Source102:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-CN.xpi
#!RemoteAsset:  sha256:757795d2e564d435c680d28b30690184a0f456148e366eabe89a2b86799a007f
Source103:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-TW.xpi
# What if firefox add another language? We should start at 200 - 251
# https://www.chromium.org/developers/how-tos/api-keys/
# Note: This key is for openRuyi use ONLY.
# For your own distribution, please get your own set of keys.
Source200:      google-api-key
Source201:      firefox.desktop
Source202:      firefox.js
Source203:      distribution.ini.in
Source204:      firefox.xml
Source205:      run-wayland-compositor.sh

BuildRequires:  appstream-glib
BuildRequires:  autoconf
BuildRequires:  cargo
BuildRequires:  cbindgen
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake(LLVM)
BuildRequires:  compiler-rt
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  nodejs
BuildRequires:  pciutils
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vpx)
# We can't remove this because of desktop_capture_gn:
#    modules/desktop_capture/linux/x11/screen_capturer_x11.h
# This header will include <X11/extensions/Xdamage.h>
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rust
BuildRequires:  unzip
BuildRequires:  zip
# For PGO desktop
#BuildRequires:  kscreenlocker
BuildRequires:  kf6-kconfig
BuildRequires:  kf6-kwallet
BuildRequires:  kwin
BuildRequires:  desktop-file-utils

Requires:       ffmpeg

%patchlist
# https://bugzilla.mozilla.org/show_bug.cgi?id=1865601
2000-riscv64-enable-gles-rendering.patch
2001-blindly-set-rust-rva23-target-when-needed.patch
2002-add-riscv64-support-for-crash-context.patch
2003-enable-crashreporter-for-riscv64.patch
# https://github.com/ggml-org/ggml/pull/1571
# Rebased onto third_party/llama.cpp (ggml-cpu.c is ggml-cpu-c.c there);
# arch/riscv/repack.cpp and llamafile/sgemm.cpp hunks dropped, not vendored.
2004-riscv64-ggml-gate-RVV-code-on-the-target-extension.patch

%description
Mozilla Firefox is a free, open-source web browser developed by
the Mozilla Foundation, focused on user privacy, speed, and
customization.

%prep
%autosetup -p1 -n %{name}-%{version}

%conf
# Configure build file for openRuyi (Globally)
cat > .mozconfig <<EOF
# Release & Branding
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1
ac_add_options --enable-update-channel=release

# Install directories
mk_add_options MOZ_OBJDIR=${PWD@Q}/obj
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --includedir=%{_includedir}

# Updater
ac_add_options --disable-updater
# Addon sideload
ac_add_options --allow-addon-sideload
ac_add_options --with-unsigned-addon-scopes=app,system

# Debug Symbols
# Normally we disable debug build because of the build time... - 251
ac_add_options --disable-debug
# But we need debug symbols
ac_add_options --enable-debug-symbols
# Let rpm do it's job - 251
ac_add_options --disable-strip
ac_add_options --disable-install-strip

# Optimization related
ac_add_options --enable-optimize
ac_add_options --enable-hardening
ac_add_options --enable-rust-simd
# Build
ac_add_options --enable-linker=lld

# Use system libraries
ac_add_options --with-system-gbm
ac_add_options --with-system-jpeg
ac_add_options --with-system-libdrm
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-pipewire
ac_add_options --with-system-webp
ac_add_options --with-system-zlib
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

# Multimedia & network related
ac_add_options --enable-pulseaudio
ac_add_options --enable-libproxy

# We use wayland
ac_add_options --enable-default-toolkit=cairo-gtk3-wayland

# sandbox libraries
ac_add_options --without-wasm-sandboxed-libraries

# Google Services
# Not free anymore... - 251
#ac_add_options --with-google-location-service-api-keyfile=%{SOURCE200}
ac_add_options --with-google-safebrowsing-api-keyfile=%{SOURCE200}

# Firefox crash reporter
ac_add_options --enable-crashreporter
# Misc
ac_add_options --disable-bootstrap
ac_add_options --disable-tests
# Enable SpiderMonkey JS shell
ac_add_options --enable-js-shell
EOF

# Some optimization related - 251
echo "ac_add_options --enable-lto" >> .mozconfig

%if %{with official_branding}
echo "ac_add_options --enable-official-branding" >> .mozconfig
%endif

# Some libraries we don't have but i think we should? - 251
%if %{with fdk_aac}
echo "ac_add_options --with-system-fdk-aac" >> .mozconfig
%endif

%build
echo "export CFLAGS=\"%{optflags}\""   >> .mozconfig
echo "export CXXFLAGS=\"%{optflags}\"" >> .mozconfig
echo "export LDFLAGS=\"%{build_ldflags}\"" >> .mozconfig
echo "export LLVM_PROFDATA=\"llvm-profdata\"" >> .mozconfig
echo "export AR=\"llvm-ar\"" >> .mozconfig
echo "export NM=\"llvm-nm\"" >> .mozconfig
echo "export RANLIB=\"llvm-ranlib\"" >> .mozconfig
# Fix: Could not find libclang to generate rust bindings for C/C++
echo "ac_add_options --with-libclang-path=`llvm-config --libdir`" >> .mozconfig

# https://firefox-source-docs.mozilla.org/build/buildsystem/pgo.html
%ifarch x86_64
echo "ac_add_options MOZ_PGO=1" >> .mozconfig

cp %{SOURCE205} .
. ./run-wayland-compositor.sh
%endif

./mach build -v

%install
DESTDIR=%{buildroot} make -C obj install

install -Dm0644 %{SOURCE201} %{buildroot}%{_datadir}/applications/firefox.desktop

# Install icons
%if %{with official_branding}
for s in 16 22 24 32 48 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp -p browser/branding/official/default${s}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/firefox.png
done
%else
for s in 16 22 24 32 48 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp -p browser/branding/unofficial/default${s}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/firefox.png
done
%endif

# We use %lang() for langpacks
echo > %{name}.lang
mkdir -p %{buildroot}%{_libdir}/firefox/langpacks
for langpack in %{_sourcedir}/*.xpi; do
    language="$(basename "$langpack" .xpi)"
    extensionID="langpack-$language@firefox.mozilla.org"

    rm -rf "$extensionID" "${extensionID}.xpi"
    mkdir -p "$extensionID"
    unzip -qq "$langpack" -d "$extensionID"
    find "$extensionID" -type f | xargs chmod 644

    cd "$extensionID"
    zip -qq -r9mX "../${extensionID}.xpi" .
    cd -

    install -m 644 "${extensionID}.xpi" %{buildroot}%{_libdir}/firefox/langpacks
    language="$(echo "$language" | sed -e 's/-/_/g')"
    echo "%%lang($language) %{_libdir}/firefox/langpacks/${extensionID}.xpi" >> %{name}.lang
done

# Install langpack workaround
function create_default_langpack() {
    language_long=$1
    language_short=$2
    cd %{buildroot}%{_libdir}/firefox/langpacks
    ln -s langpack-$language_long@firefox.mozilla.org.xpi langpack-$language_short@firefox.mozilla.org.xpi
    cd -
    echo "%%lang($language_short) %{_libdir}/firefox/langpacks/langpack-$language_short@firefox.mozilla.org.xpi" >> %{name}.lang
}

# Table of fallbacks for each language
create_default_langpack "es-AR" "es"
create_default_langpack "fy-NL" "fy"
create_default_langpack "ga-IE" "ga"
create_default_langpack "gu-IN" "gu"
create_default_langpack "hi-IN" "hi"
create_default_langpack "hy-AM" "hy"
create_default_langpack "nb-NO" "nb"
create_default_langpack "nn-NO" "nn"
create_default_langpack "pa-IN" "pa"
create_default_langpack "pt-PT" "pt"
create_default_langpack "sv-SE" "sv"
create_default_langpack "zh-TW" "zh"

# Default config
mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/preferences
cp %{SOURCE202} %{buildroot}%{_libdir}/firefox/browser/defaults/preferences

# Add distribution.ini
mkdir -p %{buildroot}%{_libdir}/firefox/distribution
sed -e "s/__NAME__/%(source /etc/os-release; echo ${NAME})/" \
    -e "s/__ID__/%(source /etc/os-release; echo ${ID})/" \
    %{SOURCE203} > %{buildroot}%{_libdir}/firefox/distribution/distribution.ini

# Install appdata
# https://bugzilla.mozilla.org/show_bug.cgi?id=1071061
# We modify the upstream one here
mkdir -p %{buildroot}%{_datadir}/metainfo
sed -e "s/__VERSION__/%{version}/" \
    -e "s/__DATE__/$(date '+%F')/" \
    %{SOURCE204} > %{buildroot}%{_datadir}/metainfo/firefox.appdata.xml

# Install license file
install -Dpm0644 LICENSE %{buildroot}%{_libdir}/firefox

# Directory for system extensions
mkdir -p %{buildroot}%{_datadir}/mozilla/extensions/\{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
mkdir -p %{buildroot}%{_libdir}/mozilla/extensions/\{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

# Use the system hunspell dictionaries
rm -rf %{buildroot}%{_libdir}/firefox/dictionaries
ln -s %{_datadir}/hunspell %{buildroot}%{_libdir}/firefox/dictionaries

# Delete unwanted files
rm -f %{buildroot}%{_libdir}/firefox/update-settings.ini
rm -f %{buildroot}%{_libdir}/firefox/removed-files

# There's no reason for any check, we already using PGO.
%check

%preun
# is it a final removal?
if [ $1 -eq 0 ]; then
    rm -rf %{_libdir}/firefox/components
    rm -rf %{_libdir}/firefox/extensions
    rm -rf %{_libdir}/firefox/plugins
    rm -rf %{_libdir}/firefox/langpacks
fi

%files -f %{name}.lang
%license %{_libdir}/firefox/LICENSE
%dir %{_datadir}/mozilla/extensions/*
%dir %{_libdir}/mozilla/extensions/*
%dir %{_libdir}/firefox/langpacks
%{_bindir}/firefox
%{_libdir}/firefox/application.ini
%{_libdir}/firefox/browser
%{_libdir}/firefox/crashreporter
%{_libdir}/firefox/crashhelper
%{_libdir}/firefox/defaults/pref/channel-prefs.js
%{_libdir}/firefox/dependentlibs.list
%{_libdir}/firefox/dictionaries
%{_libdir}/firefox/distribution
%{_libdir}/firefox/firefox
%{_libdir}/firefox/firefox-bin
%{_libdir}/firefox/fonts/TwemojiMozilla.ttf
%{_libdir}/firefox/gfxtest
%{_libdir}/firefox/gmp-clearkey
%{_libdir}/firefox/omni.ja
%{_libdir}/firefox/pingsender
%{_libdir}/firefox/platform.ini
%{_libdir}/firefox/*.so
%{_datadir}/applications/firefox.desktop
%{_datadir}/icons/hicolor/16x16/apps/firefox.png
%{_datadir}/icons/hicolor/22x22/apps/firefox.png
%{_datadir}/icons/hicolor/24x24/apps/firefox.png
%{_datadir}/icons/hicolor/256x256/apps/firefox.png
%{_datadir}/icons/hicolor/32x32/apps/firefox.png
%{_datadir}/icons/hicolor/48x48/apps/firefox.png
%{_datadir}/metainfo/firefox.appdata.xml

%changelog
%autochangelog
