{
  'targets': [
    {
      'target_name': 'node_xslt',
      'sources': [ 'node_xslt.cc' ],
      'link_settings': {
        'libraries': [
          '-lxml2',
          '-lxslt',
          '-lexslt'
          ]
      },
      'cflags': [
        '<!@(xml2-config --cflags)',
        '-fexceptions'
      ],
      'cflags_cc': ['-fexceptions'],
      'conditions': [
        ['OS=="win"', {
          # no Windows support yet...
        }, {
          'libraries': [
            '<!@(xml2-config --libs)'
          ],
        }],
        ['OS=="mac"', {
          # cflags on OS X are stupid and have to be defined like this
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '<!@(xml2-config --cflags)','-fexceptions'
            ]
          }
        }, {
          'cflags': [
            '<!@(xml2-config --cflags)','-fexceptions'
          ],
        }]
      ]
    }
  ]
}
