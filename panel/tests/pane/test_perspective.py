from panel.pane import Perspective

data = {
    0: ['1981 01 01 00   161    28 10173   270    21     0     0     0',
        '1981 01 01 01   111    33 10175   270    21     0     0 -9999',
        '1981 01 01 02   111    39 10183   330    26     0     0 -9999',
        '1981 01 01 03    94    39 10192 -9999     0     0     0 -9999',
        '1981 01 01 04    72    39 10196 -9999     0     0     0 -9999'],
    'year': [1981, 1981, 1981, 1981, 1981],
 }


def test_perspective_int_cols():
    psp = Perspective(
        data, columns=[0], aggregates={0: 'mean'}, sort=[[0, 'desc']],
        row_pivots=[0], column_pivots=[0], filters=[[0, '==', 'None']]
    )

    model = psp.get_root()
    assert '0' in model.source.data
    assert model.columns == ['0']
    assert model.row_pivots == ['0']
    assert model.column_pivots == ['0']
    assert model.aggregates == {'0': 'mean'}
    assert model.filters == [['0', '==', 'None']]
    assert model.sort == [['0', 'desc']]

    psp2 = Perspective(data)
    
    psp2._process_events({
        'columns': ['0'],
        'row_pivots': ['0'],
        'column_pivots': ['0'],
        'aggregates': {'0': 'mean'},
        'filters': [['0', '==', 'None']],
        'sort': [['0', 'desc']]
    })

    assert psp2.columns == [0]
    assert psp2.row_pivots == [0]
    assert psp2.column_pivots == [0]
    assert psp2.aggregates == {0: 'mean'}
    assert psp2.sort == [[0, 'desc']]
    assert psp2.filters == [[0, '==', 'None']]
